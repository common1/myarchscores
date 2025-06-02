import uuid

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This model can be used to add additional fields or methods in the future.
    Currently, it inherits all fields and methods from AbstractUser.
    It is recommended to use this model for user-related operations
    to maintain consistency and flexibility in the application.
    """
    pass

class BaseModel(models.Model):
    """
    Base model that includes common fields for all models.
    This model is intended to be inherited by other models to avoid code duplication.
    It provides fields for tracking creation and modification timestamps.
    The created_at field is set to the current time when the model instance is created,
    and the modified_at field is automatically updated to the current time whenever the model instance is saved.
    This is useful for auditing and tracking changes to model instances.
    The BaseModel is abstract, meaning it will not create a separate table in the database,
    """

    # created_at is a DateTimeField that stores the creation time of the model instance.
    # It is set to the current time when the model instance is created.
    # This field is not editable and is automatically set to the current time.
    # It is useful for tracking when the instance was created.
    # This field is set to not editable to prevent accidental changes after creation.
    # it is used as a base class for other models.
    # This allows other models to inherit these common fields without duplicating code.
    # This is useful for auditing and tracking changes to model instances.
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    # modified_at is a DateTimeField that stores the last modification time of the model instance.
    # It is automatically updated to the current time whenever the model instance is saved.
    # This field is editable and is automatically set to the current time on each save.
    # It is useful for tracking when the instance was last modified.
    # This field is set to auto_now=True, which means it will be updated to the current time
    # every time the model instance is saved.
    # This is useful for auditing and tracking changes to model instances.
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the BaseModel.
        """

        abstract = True

class Archer(BaseModel):
    """
    Model representing an archer.
    """

    # id is a UUID field that serves as the primary key for the Archer model.
    # It is automatically generated and not editable.
    # This ensures that each archer has a unique identifier.
    # UUIDField is used to generate a universally unique identifier for each archer.
    # This is useful for ensuring that each archer can be uniquely identified across the application.
    # The default value is set to uuid.uuid4(), which generates a new UUID each time a new archer is created.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # last_name is a CharField that stores the last name of the archer.
    # It is required and cannot be blank.
    # The last_name field is not unique, allowing multiple archers to have the same last name.
    # This is useful for cases where multiple archers may share the same last name.
    # It is a CharField with a maximum length of 64 characters which is sufficient for most last names.
    # It is not allowed to be null or blank, ensuring that every archer has a last name.
    last_name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("last name of archer"),
        help_text=_("format: required, max-64")
    )

    # first_name is a CharField that stores the first name of the archer.
    # It is required and cannot be blank.
    # The first_name field is not unique, allowing multiple archers to have the same first name.
    # This is useful for cases where multiple archers may share the same first name.
    # It is a CharField with a maximum length of 32 characters which is sufficient for most first names.
    # It is not allowed to be null or blank, ensuring that every archer has a first name.
    first_name = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("first name of archer"),
        help_text=_("format: required, max-32")
    )

    # middle_name is a CharField that stores the middle name of the archer, if any.
    # It is not required and can be blank.
    # The middle_name field is not unique, allowing multiple archers to have the same middle name.
    # It is a CharField with a maximum length of 6 characters which is sufficient for most middle names.
    # It is allowed to be null or blank, meaning that archers may not have a middle name.
    # This is useful for cases where archers may not have a middle name or prefer not to include it.
    middle_name = models.CharField(
        max_length=6,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("middle name of archer"),
        help_text=_("format: not required, max-6")
    )

    # slug is an AutoSlugField that automatically generates a slug from the last name of the archer.
    # It is editable and can be used for URL-friendly representations.
    slug = AutoSlugField(populate_from='last_name',editable=True)
    # union_number is a PositiveIntegerField that stores the union number of the archer, if any.
    # It is not required and can be blank.
    # The union number is not unique, allowing multiple archers to have the same union number.
    union_number = models.PositiveIntegerField(
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("union number of archer"),
        help_text=_("format: not required")
    )
    # info is a TextField that stores additional information about the archer.
    # It is not required and can be blank.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("archer information"),
        help_text=_("format: notrequired"),
    )
    # author is a ForeignKey that links the archer to a User who created or manages the archer's profile.
    # It uses PROTECT to prevent deletion of the user if there are archers linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the archers created by a user.
    # This is useful for querying all archers associated with a specific user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='archer_author'
    )

    # Contact information

    # email is an EmailField that stores the email address of the archer.
    # It is not required and can be blank.
    # The email field is not unique, allowing multiple archers to have the same email address.
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("email address of archer"),
        help_text=_("format: not required, max-254")
    )
    # phone is a CharField that stores the phone number of the archer.
    # It is not required and can be blank.
    # The phone field is not unique, allowing multiple archers to have the same phone number.
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("phone number of archer"),
        help_text=_("format: not required, max-15")
    )
    # address is a CharField that stores the address of the archer.
    # It is not required and can be blank.
    # The address field is not unique, allowing multiple archers to have the same address.
    address = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("address of archer"),
        help_text=_("format: not required, max-128")
    )
    # city is a CharField that stores the city of the archer.
    # It is not required and can be blank.
    # The city field is not unique, allowing multiple archers to have the same city.
    city = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("city of archer"),
        help_text=_("format: not required, max-64")
    )
    # state is a CharField that stores the state or province of the archer.
    # It is not required and can be blank.
    # The state field is not unique, allowing multiple archers to have the same state or province.
    # It is useful for archers who may not have a specific state or province.
    state = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("state or province of archer"),
        help_text=_("format: not required, max-64")
    )
    # zip_code is a CharField that stores the zip code of the archer.
    zip_code = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("zip code of archer"),
        help_text=_("format: not required, max-6")
    )
    # Contact information end

    # Extra information

    # birth_date is a DateField that stores the birth date of the archer, if provided.
    birth_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("birth date of archer"),
        help_text=_("format: Y-m-d, not required"),
    )
    # Extra information end

    class Meta:
        # Meta options for the Archer model.

        # db_table specifies the name of the database table for this model.
        # This is useful for database management and migrations.
        db_table = 'archer'

        # Ordering by last name for better readability in lists.
        # This ensures that when querying for archers, they will be sorted by their last name.
        # This is useful for displaying lists of archers in a user-friendly manner.
        # The ordering can be overridden in queries if needed.
        # It is a good practice to order models by a field that is commonly used for identification.
        ordering = ['last_name']

        # verbose_name is the singular name for the Archer model.
        verbose_name = _("Archer")

        # verbose_name_plural is the plural name for the Archer model.
        verbose_name_plural = _("Archers")

    def __init__(self, *args, **kwargs):
        """ Initialize the Archer model and set the slug field to populate from last_name."""
        super().__init__(*args, **kwargs)
        self._meta.get_field('slug').populate_from = 'last_name'

    def __str__(self):
        """ Return a string representation of the Archer model."""
        # If middle_name is provided, include it in the string representation.
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

    def __unicode__(self):
        """ Return a unicode representation of the Archer model."""
        # If middle_name is provided, include it in the unicode representation.
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

class Club(BaseModel):
    """
    Model representing an archery club.
    """
    # id is a UUID field that serves as the primary key for the Club model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # name is a CharField that stores the name of the club.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("club name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the club.
    slug = AutoSlugField(populate_from='name',editable=True)

    # town is a CharField that stores the name of the town where the club is located.
    # It is not required and can be blank.
    town = models.CharField(
        max_length=64,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("town name"),
        help_text=_("format: not required, max-64")
    )

    # archers is a ManyToManyField that links the Club model to the Archer model through the Membership model.
    # This allows multiple archers to be associated with a club and vice versa.
    archers = models.ManyToManyField(
        Archer,
        through='Membership',
        blank=True,
        help_text=_("format: not required"),
        related_name='clubs'
    )

    # info is a TextField that stores additional information about the club.
    # It is not required and can be blank.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("club information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the club to a User who created or manages the club's profile.
    # It uses PROTECT to prevent deletion of the user if there are clubs linked to them.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='author_club'
    )

    class Meta:
        # Meta options for the Club model.

        # db_table specifies the name of the database table for this model.
        db_table = 'club'

        # Ordering by name for better readability in lists.
        ordering = ['name']

        # verbose_name is the singular name for the Club model.
        verbose_name = _("Club")

        # verbose_name_plural is the plural name for the Club model.
        verbose_name_plural = _("Clubs")

    def __str__(self):
        """
        Return a string representation of the Club model.
        """
        return self.name

    def __unicode__(self):
        """
        Return a unicode representation of the Club model.
        """
        return self.name

class Membership(BaseModel):
    """
    Model representing a membership of an archer in a club.
    """

    # id is a UUID field that serves as the primary key for the Membership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # club is a ForeignKey that links the Membership model to the Club model.
    club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("club of the member"),
        help_text=_("format: required"),
        related_name='memberships'
    )

    # archer is a ForeignKey that links the Membership model to the Archer model.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archer who is member"),
        help_text=_("format: required"),
        related_name='clubmember_archer'
    )

    # start_date is a DateField that stores the start date of the membership.
    # It is not required and can be blank.
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )

    # end_date is a DateField that stores the end date of the membership.
    # It is not required and can be blank.
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )

    def __str__(self):
        """
        Return a string representation of the Membership model.
        """
        # Use the string representation of the archer and club to create a meaningful description.
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

    def __unicode__(self):
        """
        Return a unicode representation of the Membership model.
        """
        # Use the string representation of the archer and club to create a meaningful description.
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

class Category(BaseModel):
    """
    Model representing a category of archers.
    """
    # id is a UUID field that serves as the primary key for the Category model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a CharField that stores the name of the category.
    # It is required and cannot be blank.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required, max-64")
    )
    # slug is an AutoSlugField that automatically generates a slug from the name of the category.
    # It is editable and can be used for URL-friendly representations.
    slug = AutoSlugField(populate_from='name',editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='CategoryMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='categories'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("category information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='category_author'
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class CategoryMembership(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("categorymembership category"),
        help_text=_("format: required"),
        related_name='categorymemberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("categorymembership archer"),
        help_text=_("format: required"),
        related_name='categorymembership_archer'
    )

    def __str__(self):
        return f"{str(self.archer)} - {str(self.category)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.category)}"

class BowType(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("bow type name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='bowtypes'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bow type information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowtype_author'
    )
    
    # Specific fields
    type_of_bow = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bow type"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("recurve", "Recurve"),
            ("compound", "Compound"),
            ("longbow", "Longbow"),
            ("barebow", "Barebow"),
            ("crossbow", "Crossbow"),
            ("other", "Other")
        ]
    )
    max_draw_weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("maximum draw weight"),
        help_text=_("format: not required"),
    )
    min_draw_weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("minimum draw weight"),
        help_text=_("format: not required"),
    )
    max_draw_length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("maximum draw length in inches"),
        help_text=_("format: not required"),
    )
    min_draw_length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("minimum draw length in inches"),
        help_text=_("format: not required"),
    )
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bow length in inches"),
        help_text=_("format: not required"),
    )
    color = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bow color"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("black", "Black"),
            ("brown", "Brown"),
            ("white", "White"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow"),
            ("other", "Other")
        ]
    )
    material = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bow material"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("wood", "Wood"),
            ("carbon", "Carbon"),
            ("aluminum", "Aluminum"),
            ("fiberglass", "Fiberglass"),
            ("composite", "Composite"),
            ("other", "Other")
        ]
    )
    # Specific fields end  

        
    class Meta:
        verbose_name = _("Bow Type")
        verbose_name_plural = _("Bow Types")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class BowTypeMembership(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowtypemembership bowtype"),
        help_text=_("format: required"),
        related_name='bowtypememberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowtypemembership archer"),
        help_text=_("format: required"),
        related_name='bowtypemembership_archer'
    )

    def __str__(self):
        return f"{str(self.archer)} - {str(self.bowtype)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.bowtype)}"

class BowString(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("bowstring name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowstring bowtype"),
        help_text=_("format: required"),
        related_name='bowstrings'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowstring information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowstring_author'
    )

    # Extra fields
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowstring length in inches"),
        help_text=_("format: not required"),
    )
    color = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowstring color"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("black", "Black"),
            ("brown", "Brown"),
            ("white", "White"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow"),
            ("other", "Other")
        ]
    )
    material = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowstring material"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("dacron", "Dacron"),
            ("fastflight", "FastFlight"),
            ("other", "Other")
        ]
    )
    # Extra fields end
    
    class Meta:
        verbose_name = _("Bow String")
        verbose_name_plural = _("Bow Strings")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class BowRiser(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("bowriser name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowriser bowtype"),
        help_text=_("format: required"),
        related_name='bowrisers'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowriser information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowriser_author'
    )

    # Extra fields
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowriser length in inches"),
        help_text=_("format: not required"),
    )
    color = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowriser color"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("black", "Black"),
            ("brown", "Brown"),
            ("white", "White"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow"),
            ("other", "Other")
        ]
    )
    material = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowriser material"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("wood", "Wood"),
            ("carbon", "Carbon"),
            ("aluminum", "Aluminum"),
            ("fiberglass", "Fiberglass"),
            ("composite", "Composite"),
            ("other", "Other")
        ]
    )
    # Extra fields end
    
    class Meta:
        verbose_name = _("Bow Riser")
        verbose_name_plural = _("Bow Risers")

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class BowLimb(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("bowlimb name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowlimb bowtype"),
        help_text=_("format: required"),
        related_name='bowlimbs'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowlimb information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowlimb_author'
    )

    # Extra fields
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowlimb length in inches"),
        help_text=_("format: not required"),
    )
    color = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowlimb color"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("black", "Black"),
            ("brown", "Brown"),
            ("white", "White"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow"),
            ("other", "Other")
        ]
    )
    material = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowlimb material"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("wood", "Wood"),
            ("carbon", "Carbon"),
            ("aluminum", "Aluminum"),
            ("fiberglass", "Fiberglass"),
            ("composite", "Composite"),
            ("other", "Other")
        ]
    )
    # Tension is the force applied to the bow limb when drawn, measured in pounds.
    tension = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowlimb tension in pounds"),
        help_text=_("format: not required"),
    )
    # Draw weight is the weight required to draw the bow limb to its full draw length, measured in pounds.
    draw_weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowlimb draw weight in pounds"),
        help_text=_("format: not required"),
    )
    draw_weight_range = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowlimb draw weight range"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("20-30 lbs", "20-30 lbs"),
            ("30-40 lbs", "30-40 lbs"),
            ("40-50 lbs", "40-50 lbs"),
            ("50-60 lbs", "50-60 lbs"),
            ("60+ lbs", "60+ lbs"),
            ("other", "Other")
        ]
    )
    # Draw length is the distance from the bowstring to the back of the bow limb when drawn, measured in inches.
    draw_length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowlimb draw length in inches"),
        help_text=_("format: not required"),
    )
    # Draw length range is the range of draw lengths that the bow limb can accommodate, measured in inches.
    draw_length_range = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowlimb draw length range"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("24-26 inches", "24-26 inches"),
            ("26-28 inches", "26-28 inches"),
            ("28-30 inches", "28-30 inches"),
            ("30+ inches", "30+ inches"),
            ("other", "Other")
        ]
    )
    # Limb type indicates whether the limb is a top limb or bottom limb.
    limb_type = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        verbose_name=_("bowlimb type"),
        help_text=_("format: not required, max-16"),
        choices=[
            ("top", "Top Limb"),
            ("bottom", "Bottom Limb"),
            ("other", "Other")
        ]
    )
    # Limb weight is the weight of the bow limb itself, measured in pounds.
    limb_weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowlimb weight in pounds"),
        help_text=_("format: not required"),
    )
    # Limb weight range is the range of weights that the bow limb can accommodate, measured in pounds.
    limb_weight_range = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowlimb weight range"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("1-2 lbs", "1-2 lbs"),
            ("2-3 lbs", "2-3 lbs"),
            ("3-4 lbs", "3-4 lbs"),
            ("4+ lbs", "4+ lbs"),
            ("other", "Other")
        ]
    )
    # Extra fields end

    class Meta:
        verbose_name = _("Bow Limb")
        verbose_name_plural = _("Bow Limbs")

    def __str__(self):
       return

class Team(BaseModel):
    '''Model representing a team of archers.'''

    '''id is a UUID field that serves as the primary key for the Team model.'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("team name"),
        help_text=_("format: required, max-64")
    )
    '''slug is a unique identifier for the team, automatically generated from the name.'''
    slug = AutoSlugField(populate_from='name',editable=True)
    '''archer is a many-to-many relationship with the Archer model, allowing multiple archers to be part of a team.'''
    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='teams'
    )
    '''info is a text field for additional information about the team.'''
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("team information"),
        help_text=_("format: not required"),
    )
    '''author is a foreign key to the User model, indicating who created the team.'''
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='team_author'
    )

    class Meta:
        '''verbose_name is the singular name for the Team model.'''
        verbose_name = _("Team")
        '''verbose_name_plural is the plural name for the Team model.'''
        verbose_name_plural = _("Teams")

    def __str__(self):
        '''Returns the name of the team.'''
        return self.name

    def __unicode__(self):
        '''Returns the name of the team in unicode format.'''
        return self.name

class TeamMembership(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("teammembership team"),
        help_text=_("format: required"),
        related_name='teammemberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("teammembership archer"),
        help_text=_("format: required"),
        related_name='teammembership_archer'
    )

    def __str__(self):
        return f"{str(self.archer)} - {str(self.team)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.team)}"

class Contest(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("contest name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='contests'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("contest information"),
        help_text=_("format: not required"),
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start date of contest"),
        help_text=_("format: Y-m-d, not required"),
    )
    start_time = models.TimeField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start time of contest"),
        help_text=_("format: H:M:S, not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='contest_author'
    )

    class Meta:
        verbose_name = _("Contest")
        verbose_name_plural = _("Contests")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class ContestMembership(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contest = models.ForeignKey(
        Contest,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("contestmembership contest"),
        help_text=_("format: required"),
        related_name='contestmemberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("contestmembership archer"),
        help_text=_("format: required"),
        related_name='contestmembership_archer'
    )

    def __str__(self):
        return f"{str(self.archer)} - {str(self.contest)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.contest)}"

TARGET_DIAMETERS = (
    ("40 cm", "40 cm"),
    ("60 cm", "60 cm"),
    ("80 cm", "80 cm"),
    ("122 cm", "122 cm"),
)

class TargetFace(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("targetface name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    diameter = models.CharField (
        null=False,
        unique=False,
        blank=False,
        choices=TARGET_DIAMETERS,
        default="40",
        max_length=32,
        verbose_name=_("diameter of targetface"),
        help_text=_("format: required, max-32")
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("targetface information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='targetface_author'
    )

    class Meta:
        verbose_name = _("Target Face")
        verbose_name_plural = _("Target Faces")

    def __str__(self):
        return f"{self.name} ( {self.diameter} )"

    def __unicode__(self):
        return f"{self.name} ( {self.diameter} )"

SHEET_DIMENSIONS = (
    ("10x3", "10x3"),
    ("5x5", "5x5"),
)

class ScoringSheet(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("scoringsheet name"),
        help_text=_("format: not required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    dimension = models.CharField (
        null=True,
        unique=False,
        blank=True,
        choices=SHEET_DIMENSIONS,
        default="10x3",
        max_length=5,
        verbose_name=_("dimension of scoringsheet"),
        help_text=_("format: required, max-5")
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("scoringsheet information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='scoringsheet_author'
    )

    class Meta:
        verbose_name = _("Scoring Sheet Type")
        verbose_name_plural = _("Scoring Sheet Types")

    def __str__(self):
        return f"{self.name} ( {self.dimension} )"

    def __unicode__(self):
        return f"{self.name} ( {self.dimension} )"

class Result(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    archer=models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("archer who shot the score"),
        help_text=_("format: not required"),
        related_name='result_archer'
    )
    contest=models.ForeignKey(
        Contest,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("contest of the score"),
        help_text=_("format: not required"),
        related_name='result_contest'
    )
    targetface = models.ForeignKey(
        TargetFace,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("targetface used"),
        help_text=_("format: not required"),
        related_name='result_targetface'
    )
    scoringsheet = models.ForeignKey(
        ScoringSheet,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("scoringsheet used"),
        help_text=_("format: not required"),
        related_name='result_scoringsheet'
    )
    score=models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("nr of points shot"),
        help_text=_("format: not required"),
    )
    slug = AutoSlugField(populate_from='score',editable=True)
    arrows=models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("nr of arrows shot"),
        help_text=_("format: not required"),
    )
    distance=models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("shooting distance in meters"),
        help_text=_("format: not required"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("result information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='result_author'
    )

    class Meta:
        verbose_name = _("Result")
        verbose_name_plural = _("Results")

    def __str__(self):
        return str(self.score)

    def __unicode__(self):
        return str(self.score)

    @property
    def average(self):
        result = None

        if self.score and self.arrows:
            if (self.arrows > 0):
                result = round(self.score / self.arrows, 2)

        return result

class Competition(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("competition name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='competitions'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("competition information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='competition_author'
    )

    class Meta:
        verbose_name = _("Competition")
        verbose_name_plural = _("Competitions")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class CompetitionMembership(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    competition = models.ForeignKey(
        Competition,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("competitionmembership competition"),
        help_text=_("format: required"),
        related_name='competitionmemberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("competitionmembership archer"),
        help_text=_("format: required"),
        related_name='competitionmembership_archer'
    )

    def __str__(self):
        return f"{str(self.archer)} - {str(self.competition)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.competition)}"

class Arrow(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("arrow name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("arrow information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='arrow_author'
    )

    # Specific fields
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("arrow length in inches"),
        help_text=_("format: not required"),
    )
    diameter = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("arrow diameter in mm"),
        help_text=_("format: not required"),
    )
    spine = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("arrow spine"),
        help_text=_("format: not required"),
    )
    weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("arrow weight in grains"),
        help_text=_("format: not required"),
    )

    class Meta:
        verbose_name = _("Arrow")
        verbose_name_plural = _("Arrows")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class Fletching(BaseModel):
    """
    Model representing a fletching used in archery arrows.
    """
    # id is a UUID field that serves as the primary key for the Fletching model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the fletching, which is a part of the arrow that stabilizes its flight.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("fletching name"),
        help_text=_("format: required, max-64")
    )
    # slug is a unique identifier for the fletching, automatically generated from the name.
    slug = AutoSlugField(populate_from='name',editable=True)
    # arrow is a many-to-many relationship with the Arrow model, allowing multiple arrows to be associated with a fletching.
    arrow = models.ManyToManyField(
        Arrow,
        blank=True,
        help_text=_("format: not required"),
        related_name='fletchings'
    )
    # info is a text field for additional information about the fletching.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("fletching information"),
        help_text=_("format: not required"),
    )
    # author is a foreign key to the User model, indicating who created the fletching.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='fletching_author'
    )

    # Specific fields
    # Fletching color is the color of the fletching, which can affect arrow visibility and flight characteristics.
    color = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("fletching color"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("black", "Black"),
            ("brown", "Brown"),
            ("white", "White"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow"),
            ("other", "Other")
        ]
    )
    # Fletching material is the type of material used for the fletching, which can affect arrow flight and stability.
    material = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("fletching material"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("feather", "Feather"),
            ("plastic", "Plastic"),
            ("other", "Other")
        ]
    )
    # Fletching length is the length of the fletching, which can affect arrow flight and stability.
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching length in inches"),
        help_text=_("format: not required"),
    )
    # Fletching width is the width of the fletching, which can affect arrow flight and stability.
    width = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching width in inches"),
        help_text=_("format: not required"),
    )
    # Fletching height is the height of the fletching, which can affect arrow flight and stability.
    height = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching height in inches"),
        help_text=_("format: not required"),
    )
    # Fletching weight is the weight of the fletching, which can affect arrow flight and stability.
    weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching weight in grains"),
        help_text=_("format: not required"),
    )
    # Fletching thickness is the thickness of the fletching material, which can affect arrow flight and stability.
    thickness = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching thickness in mm"),
        help_text=_("format: not required"),
    )
    # Fletching position is the position of the fletching on the arrow shaft, measured in inches from the nock end.
    position = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching position in inches"),
        help_text=_("format: not required"),
    )
    # Fletching orientation is the direction in which the fletching is attached to the arrow shaft.
    orientation = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        verbose_name=_("fletching orientation"),
        help_text=_("format: not required, max-16"),
        choices=[
            ("right", "Right Wing"),
            ("left", "Left Wing"),
            ("straight", "Straight"),
            ("other", "Other")
        ]
    )
    # Fletching angle is the angle at which the fletching is attached to the arrow shaft, measured in degrees.
    angle = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("fletching angle in degrees"),
        help_text=_("format: not required"),
    )
    # Fletching type is the shape of the fletching, which can affect arrow flight and stability.
    fletching_type = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("fletching type"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("shield", "Shield"),
            ("parabolic", "Parabolic"),
            ("banana", "Banana"),
            ("other", "Other")
        ]
    )

    class Meta:
       verbose_name = _("Fletching")
       verbose_name_plural = _("Fletchings")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class ArrowFletching(BaseModel):
    """
    Model representing the relationship between an arrow and its fletching.
    """

    # id is a UUID field that serves as the primary key for the ArrowFletching model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # arrow is a foreign key to the Arrow model, indicating which arrow is being fletched.
    arrow = models.ForeignKey(
        Arrow,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("arrowfletching arrow"),
        help_text=_("format: required"),
        related_name='arrowfletchings'
    )
    # fletching is a foreign key to the Fletching model, indicating which fletching is being used on the arrow.
    fletching = models.ForeignKey(
        Fletching,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("arrowfletching fletching"),
        help_text=_("format: required"),
        related_name='arrowfletching_fletching'
    )
    # author is a foreign key to the User model, indicating who created the arrow fletching relationship.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='arrowfletching_author'
    )

    class Meta:
        # verbose_name is the singular name for the ArrowFletching model.
        verbose_name = _("Arrow Fletching")
        # verbose_name_plural is the plural name for the ArrowFletching model.
        verbose_name_plural = _("Arrow Fletchings")

    def __str__(self):
        """
        Returns a string representation of the ArrowFletching instance.
        This representation includes the arrow and fletching names.
        """
        return f"{str(self.arrow)} - {str(self.fletching)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the ArrowFletching instance.
        This representation includes the arrow and fletching names.
        """
        return f"{str(self.arrow)} - {str(self.fletching)}"

