from rlbot.training.training import Pass, Fail

from rlbottraining.grading.grader import Grader
from rlbottraining.grading.event_detector import PlayerEventType
from rlbottraining.grading.training_tick_packet import TrainingTickPacket
from rlbottraining.common_graders.compound_grader import CompoundGrader
from rlbottraining.common_graders.timeout import FailOnTimeout, PassOnTimeout


class StrikerGrader(CompoundGrader):
    """
    A Grader which acts similarly to the RocketLeague striker training.
    """

    def __init__(self, timeout_seconds=4.0, ally_team=0):
        super().__init__([
            PassOnGoalForAllyTeam(ally_team),
            FailOnTimeout(timeout_seconds),
        ])


class GoalieGrader(CompoundGrader):
    """
    A Grader which acts similarly to the RocketLeague goalie training.
    """

    def __init__(self, timeout_seconds=10.0, ally_team=0):
        super().__init__([
            PassOnBallGoingAwayFromGoal(ally_team),
            PassOnGoalForAllyTeam(ally_team),
            PassOnTimeout(timeout_seconds),
        ])


class WrongGoalFail(Fail):
    def __repr__(self):
        return f'{super().__repr__()}: Ball went into the wrong goal.'


class PassOnGoalForAllyTeam(Grader):
    """
    Terminates the Exercise when any goal is scored.
    Returns a Pass iff the goal was for ally_team,
    otherwise returns a Fail.
    """

    def __init__(self, ally_team: int):
        """
        :param ally_team: number equal to game_datastruct.PlayerInfo.team.
        """
        self.ally_team = ally_team

    def on_tick(self, tick: TrainingTickPacket):
        for event in tick.player_events:
            if event.type == PlayerEventType.GOALS:
                if event.player.team == self.ally_team:
                    return Pass()
                else:
                    return WrongGoalFail()
            elif event.type == PlayerEventType.OWN_GOALS:
                if event.player.team == self.ally_team:
                    return WrongGoalFail()
                else:
                    return Pass()


class PassOnBallGoingAwayFromGoal(Grader):
    """
    Returns Pass() iff a player on the ally team prevents a goal
    and triggers the in-game "save" event.
    Never returns a Fail().
    """

    # Prevent false positives which might be caused by two bots touching the ball at basically the same time.
    REQUIRED_CONSECUTIVE_TICKS = 20

    def __init__(self, ally_team: int):
        """
        :param ally_team: number equal to game_datastruct.PlayerInfo.team.
        """
        self.ally_team = ally_team
        self.consequtive_good_ticks = 0

    def on_tick(self, tick: TrainingTickPacket):
        to_own_goal = 1 if self.ally_team == 0 else -1
        if tick.game_tick_packet.game_ball.physics.velocity.y * to_own_goal > 0:
            self.consequtive_good_ticks += 1
        else:
            self.consequtive_good_ticks = 0

        if self.consequtive_good_ticks >= self.REQUIRED_CONSECUTIVE_TICKS:
            return Pass()
