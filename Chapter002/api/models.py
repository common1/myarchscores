import uuid

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Archer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("last name of archer"),
        help_text=_("format: required, max-64")
    )
    first_name = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("first name of archer"),
        help_text=_("format: required, max-32")
    )
    middle_name = models.CharField(
        max_length=6,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("middle name of archer"),
        help_text=_("format: not required, max-6")
    )
    slug = AutoSlugField(populate_from='last_name',editable=True)
    union_number = models.PositiveIntegerField(
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("union number of archer"),
        help_text=_("format: not required")
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("archer information"),
        help_text=_("format: notrequired"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='archer_author'
    )

    class Meta:
        ordering = ['last_name']
        verbose_name = _("Archer")
        verbose_name_plural = _("Archers")

    def __str__(self):
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

    def __unicode__(self):
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

class Club(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("club name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    town = models.CharField(
        max_length=64,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("town name"),
        help_text=_("format: not required, max-64")
    )
    archers = models.ManyToManyField(
        Archer,
        through='Membership',
        blank=True,
        help_text=_("format: not required"),
        related_name='clubs'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("club information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='author_club'
    )

    class Meta:
        verbose_name = _("Club")
        verbose_name_plural = _("Clubs")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Membership(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("club of the member"),
        help_text=_("format: required"),
        related_name='clubmember_club'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archer who is member"),
        help_text=_("format: required"),
        related_name='clubmember_archer'
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )

# Extensions

# class Category(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("category name"),
#         help_text=_("format: required, max-64")
#     )
#     slug = AutoSlugField(populate_from='name',editable=True)
#     archer = models.ManyToManyField(
#         Archer,
#         blank=True,
#         help_text=_("format: not required"),
#         related_name='category_archers'
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("category information"),
#         help_text=_("format: not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='category_author'
#     )

#     class Meta:
#         verbose_name = _("Category")
#         verbose_name_plural = _("Categories")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name


# class Team(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         blank=False,
#         unique=False,
#         verbose_name=_("team name"),
#         help_text=_("format: required, max-64")
#     )
#     slug = AutoSlugField(populate_from='name',editable=True)
#     archer = models.ManyToManyField(
#         Archer,
#         blank=True,
#         help_text=_("format: not required"),
#         related_name='team_archers'
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("team information"),
#         help_text=_("format: not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='team_author'
#     )

#     class Meta:
#         verbose_name = _("Team")
#         verbose_name_plural = _("Teams")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Contest(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("contest name"),
#         help_text=_("format: required, max-64")
#     )
#     slug = AutoSlugField(populate_from='name',editable=True)
#     archer = models.ManyToManyField(
#         Archer,
#         blank=True,
#         help_text=_("format: not required"),
#         related_name='contest_archers'
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("contest information"),
#         help_text=_("format: not required"),
#     )
#     start_date = models.DateField(
#         null=True,
#         blank=True,
#         editable=True,
#         unique=False,
#         verbose_name=_("start date of contest"),
#         help_text=_("format: Y-m-d, not required"),
#     )
#     start_time = models.TimeField(
#         null=True,
#         blank=True,
#         editable=True,
#         unique=False,
#         verbose_name=_("start time of contest"),
#         help_text=_("format: H:M:S, not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='contest_author'
#     )

#     class Meta:
#         verbose_name = _("Contest")
#         verbose_name_plural = _("Contests")

#     def __str__(self):
#        return self.name

#     def __unicode__(self):
#        return self.name


# TARGET_DIAMETERS = (
#     ("40 cm", "40 cm"),
#     ("60 cm", "60 cm"),
#     ("80 cm", "80 cm"),
#     ("122 cm", "122 cm"),
# )

# class TargetFace(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("targetface name"),
#         help_text=_("format: required, max-64")
#     )
#     slug = AutoSlugField(populate_from='name',editable=True)
#     diameter = models.CharField (
#         null=False,
#         unique=False,
#         blank=False,
#         choices=TARGET_DIAMETERS,
#         default="40",
#         max_length=32,
#         verbose_name=_("diameter of targetface"),
#         help_text=_("format: required, max-32")
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("targetface information"),
#         help_text=_("format: not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='targetface_author'
#     )

#     class Meta:
#         verbose_name = _("Target Face")
#         verbose_name_plural = _("Target Faces")

#     def __str__(self):
#         return f"{self.name} ( {self.diameter} )"

#     def __unicode__(self):
#         return f"{self.name} ( {self.diameter} )"

# SHEET_DIMENSIONS = (
#     ("10x3", "10x3"),
#     ("5x5", "5x5"),
# )

# class ScoringSheet(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("scoringsheet name"),
#         help_text=_("format: not required, max-64")
#     )
#     slug = AutoSlugField(populate_from='name',editable=True)
#     dimension = models.CharField (
#         null=True,
#         unique=False,
#         blank=True,
#         choices=SHEET_DIMENSIONS,
#         default="10x3",
#         max_length=5,
#         verbose_name=_("dimension of scoringsheet"),
#         help_text=_("format: required, max-5")
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("scoringsheet information"),
#         help_text=_("format: not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='scoringsheet_author'
#     )

#     class Meta:
#         verbose_name = _("Scoring Sheet")
#         verbose_name_plural = _("Scoring Sheets")

#     def __str__(self):
#         return f"{self.name} ( {self.dimension} )"

#     def __unicode__(self):
#         return f"{self.name} ( {self.diameter} )"

# class Result(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     archer=models.ForeignKey(
#         Archer,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("archer who shot the score"),
#         help_text=_("format: not required"),
#         related_name='result_archer'
#     )
#     contest=models.ForeignKey(
#         Contest,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("contest of the score"),
#         help_text=_("format: not required"),
#         related_name='result_contest'
#     )
#     targetface = models.ForeignKey(
#         TargetFace,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("targetface used"),
#         help_text=_("format: not required"),
#         related_name='result_targetface'
#     )
#     scoringsheet = models.ForeignKey(
#         ScoringSheet,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("scoringsheet used"),
#         help_text=_("format: not required"),
#         related_name='result_scoringsheet'
#     )
#     amount=models.PositiveSmallIntegerField(
#         default=0,
#         null=False,
#         blank=False,
#         unique=False,
#         verbose_name=_("nr of points shot"),
#         help_text=_("format: not required"),
#     )
#     slug = AutoSlugField(populate_from='amount',editable=True)
#     arrows=models.PositiveSmallIntegerField(
#         default=0,
#         null=False,
#         blank=False,
#         unique=False,
#         verbose_name=_("nr of arrows shot"),
#         help_text=_("format: not required"),
#     )
#     distance=models.PositiveSmallIntegerField(
#         default=0,
#         null=False,
#         blank=False,
#         unique=False,
#         verbose_name=_("shooting distance in meters"),
#         help_text=_("format: not required"),
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("result information"),
#         help_text=_("format: not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='result_author'
#     )

#     class Meta:
#         verbose_name = _("Result")
#         verbose_name_plural = _("Results")

#     def __str__(self):
#         return str(self.amount)

#     def __unicode__(self):
#         return str(self.amount)

#     @property
#     def average(self):
#         result = None

#         if self.amount and self.arrows:
#             if (self.arrows > 0):
#                 result = round(self.amount / self.arrows, 2)

#         return result

# class Competition(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("competition name"),
#         help_text=_("format: required, max-64")
#     )
#     slug = AutoSlugField(populate_from='name',editable=True)
#     archer = models.ManyToManyField(
#         Archer,
#         blank=True,
#         help_text=_("format: not required"),
#         related_name='competition_archers'
#     )
#     info = models.TextField(
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("competition information"),
#         help_text=_("format: not required"),
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         default=1,
#         related_name='competition_author'
#     )

#     class Meta:
#         verbose_name = _("Competition")
#         verbose_name_plural = _("Competitions")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name
