from parenttext_pipeline.models.parenttext_models import *
from rpft.parsers.common.rowparser import ParserModel
from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.creation.models import Condition, SurveyQuestionModel


class Confirmation(ParserModel):
    condition: Condition = Condition()
    question: str = ""
    confirm_option: str = ""
    back_option: str = ""


class LocalSurveyQuestionModel(SurveyQuestionModel):
    confirmation: Confirmation = Confirmation()


class SurveyQuestionRowModel(DataRowModel, LocalSurveyQuestionModel):
    pass
