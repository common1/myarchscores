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
        This model is abstract, meaning it will not create a separate table in the database.
        It is intended to be inherited by other models to avoid code duplication.
        The abstract = True option indicates that this model should not be created as a separate table.
        Instead, it will be used as a base class for other models.
        """

        abstract = True

class Archer(BaseModel):
    """
    Model representing an archer.
    This model includes fields for personal information, contact details, and relationships with clubs and categories.
    It is designed to store information about archers in the application.
    The Archer model inherits from BaseModel to include common fields for tracking creation and modification timestamps.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Archer model and set up the slug field to be generated from the last_name field.
        This method is called when an instance of the Archer model is created.
        It allows for customization of the model's initialization process.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        # Call the parent class's __init__ method to ensure proper initialization.
        # This is necessary to ensure that the model is set up correctly.
        # This allows the slug field to be automatically generated based on the last_name field.
        # The populate_from argument specifies that the slug should be generated from the last_name field.
        # This is useful for creating URL-friendly representations of the archer's name.
        super().__init__(*args, **kwargs)
        self._meta.get_field('slug').populate_from = 'last_name'

    # id is a UUID field that serves as the primary key for the Archer model.
    # It is automatically generated and not editable.
    # This ensures that each archer has a unique identifier.
    # UUIDField is used to generate a universally unique identifier for each archer.
    # This is useful for ensuring that each archer can be uniquely identified across the application.
    # The default value is set to uuid.uuid4(), which generates a new UUID each time a new archer is created.
    # This is useful for database management and migrations.
    # It allows for easy identification of the archer in the database.
    # The id field is not editable, meaning it cannot be changed after the archer is created.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # last_name is a CharField that stores the last name of the archer.
    # It is required and cannot be blank.
    # The last_name field is not unique, allowing multiple archers to have the same last name.
    # This is useful for cases where multiple archers may share the same last name.
    # It is a CharField with a maximum length of 64 characters which is sufficient for most last names.
    # It is not allowed to be null or blank, ensuring that every archer has a last name.
    # The last_name field is editable, allowing users to change it if needed.
    # It is useful for cases where archers may want to update their last name or rebrand themselves.
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
    # The first_name field is editable, allowing users to change it if needed.
    # It is useful for cases where archers may want to update their first name or rebrand themselves.
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
    # The middle_name field is editable, allowing users to change it if needed.
    # It is useful for cases where archers may want to include their middle name or update it later.
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
    # The slug field is not unique, allowing multiple archers to have the same slug.
    # This is useful for cases where multiple archers may share the same last name.
    # The slug is generated from the last_name field, ensuring that it is always based on the archer's last name.
    # This allows for easy identification of the archer in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='last_name',editable=True)

    # union_number is a PositiveIntegerField that stores the union number of the archer.
    # It is not required and can be blank.
    # The union_number field is unique, meaning that each archer can have a different union number.
    # This is useful for cases where archers are part of a union or organization that assigns unique numbers.
    # It is a PositiveIntegerField, meaning it can only store positive integers.
    union_number = models.PositiveIntegerField(
        null=True,
        unique=True,
        blank=True,
        verbose_name=_("union number of archer"),
        help_text=_("format: not required")
    )

    # info is a TextField that stores additional information about the archer.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple archers to have the same information.
    # This is useful for cases where archers may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that archers may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("archer information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the archer to a User who created or manages the archer's profile.
    # It uses PROTECT to prevent deletion of the user if there are archers linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the archers created by a user.
    # This is useful for querying all archers associated with a specific user.
    # The author field is not unique, allowing multiple archers to be created by the same user.
    # This is useful for cases where multiple archers are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of archer"),
        related_name='archer_author',
        help_text=_("format: not required, default=1 (superuser)"),
    )

    # Contact information

    # email is an EmailField that stores the email address of the archer.
    # It is not required and can be blank.
    # The email field is not unique, allowing multiple archers to have the same email address.
    # This is useful for cases where archers may not have a specific email address or prefer not to provide one.
    # It is an EmailField with a maximum length of 254 characters, which is sufficient for most email addresses.
    # It is allowed to be null or blank, meaning that archers may not have an email address.
    # The email field is editable, allowing users to change it if needed.
    # It is useful for cases where archers may want to update their email address or provide it later.
    # verbose_name provides a human-readable name for the field in the admin interface.
    # help_text provides additional information about the field's format and requirements.
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
    # This is useful for cases where archers may not have a specific phone number or prefer not to provide one.
    # It is a CharField with a maximum length of 15 characters, which is sufficient for most phone numbers.
    # It is allowed to be null or blank, meaning that archers may not have a phone number.
    # The phone field is editable, allowing users to change it if needed.
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
    # This is useful for cases where archers may not have a specific address or prefer not to provide one.
    # It is a CharField with a maximum length of 128 characters, which is sufficient for most addresses.
    # It is allowed to be null or blank, meaning that archers may not have an address.
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
    # This is useful for archers who may not have a specific city or prefer not to provide one.
    # It is a CharField with a maximum length of 64 characters, which is sufficient for most city names.
    # It is allowed to be null or blank, meaning that archers may not have a city.
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
    # It is a CharField with a maximum length of 64 characters, which is sufficient for most state or province names.
    # It is allowed to be null or blank, meaning that archers may not have a state or province.
    state = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("state or province of archer"),
        help_text=_("format: not required, max-64")
    )

    # zip_code is a CharField that stores the zip code of the archer.
    # It is not required and can be blank.
    # The zip_code field is not unique, allowing multiple archers to have the same zip code.
    # This is useful for archers who may not have a specific zip code or prefer not to provide one.
    # It is a CharField with a maximum length of 6 characters, which is sufficient for most zip codes.
    # It is allowed to be null or blank, meaning that archers may not have a zip code.
    zip_code = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("zip code of archer"),
        help_text=_("format: not required, max-6")
    )

    # Contact information end

    # Extra fields for archer information

    # birth_date is a DateField that stores the birth date of the archer, if provided.
    # It is not required and can be blank.
    # The birth_date field is not unique, allowing multiple archers to have the same birth date.
    # This is useful for archers who may not want to provide their birth date or prefer not to include it.
    # It is a DateField, which means it stores dates in the format YYYY-MM-DD.
    # It is allowed to be null or blank, meaning that archers may not have a birth date.
    # The birth_date field is editable, allowing users to change it if needed.
    # It is useful for cases where archers may want to update their birth date or provide it later.
    birth_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("birth date of archer"),
        help_text=_("format: Y-m-d, not required"),
    )
    
    # Extra fields for archer information end
    
    class Meta:
        """
        Meta options for the Archer model.
        This model is used to represent an archer in the application.
        The Meta class allows for customization of the model's behavior and appearance.
        It includes options such as the database table name, ordering, and verbose names.
        The Archer model is used to store information about archers, including their personal details,
        contact information, and relationships with clubs and categories.
        """

        # db_table specifies the name of the database table for this model.
        # This is useful for database management and migrations.
        # It allows for easy identification of the table associated with the Archer model.
        # Using 'archer' as the table name for clarity and consistency.
        # This is useful for database management and migrations.
        db_table = 'archer'

        # Ordering by last name for better readability in lists.
        # This ensures that when querying for archers, they will be sorted by their last name.
        # This is useful for displaying lists of archers in a user-friendly manner.
        # The ordering can be overridden in queries if needed.
        # It is a good practice to order models by a field that is commonly used for identification.
        # Using 'last_name' as the field to order by for clarity and consistency.
        # This is useful for displaying lists of archers in a user-friendly manner.
        ordering = ['last_name']

        # verbose_name is the singular name for the Archer model.
        # This is used in the Django admin interface and other places where a singular name is needed.
        # It provides a human-readable name for the model.
        # Using "Archer" as the singular name for clarity and consistency.
        # This is useful for displaying the archer's name in a user-friendly manner.
        verbose_name = _("Archer")

        # verbose_name_plural is the plural name for the Archer model.
        # This is used in the Django admin interface and other places where a plural name is needed.
        # It provides a human-readable name for the model when referring to multiple instances.
        # Using "Archers" as the plural name for clarity and consistency.
        # This is useful for displaying lists of archers in a user-friendly manner.
        verbose_name_plural = _("Archers")

    def __str__(self):
        """
        Return a string representation of the Archer model.
        This method is used to provide a human-readable representation of the archer's name.
        The string representation is useful for displaying the archer's name in lists and other contexts.
    
        """

        # If middle_name is provided, include it in the string representation.
        # This allows for a more complete representation of the archer's name.
        # The string representation is useful for displaying the archer's name in lists and other contexts.
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

    def __unicode__(self):
        """
        Return a unicode representation of the Archer model.
        This method is used to provide a human-readable representation of the archer's name.
        The unicode representation is useful for displaying the archer's name in lists and other contexts.
        """

        # If middle_name is provided, include it in the unicode representation.
        # This allows for a more complete representation of the archer's name.
        # The unicode representation is useful for displaying the archer's name in lists and other contexts.
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

class Club(BaseModel):
    """
    Model representing an archery club.
    This model includes fields for club information, contact details,
    and relationships with archers.
    It is designed to store information about clubs in the application.
    The Club model inherits from BaseModel to include common fields for tracking creation and modification timestamps.
    The Club model is used to represent an archery club, which can have multiple archers associated with it.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Club model and set up the slug field to be generated from the name field.
        This method is called when an instance of the Club model is created.
        It allows for customization of the model's initialization process.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        # Call the parent class's __init__ method to ensure proper initialization.
        # This is necessary to ensure that the model is set up correctly.
        # This allows the slug field to be automatically generated based on the name field.
        # The populate_from argument specifies that the slug should be generated from the name field.
        # This is useful for creating URL-friendly representations of the club.
        super().__init__(*args, **kwargs)
        self._meta.get_field('slug').populate_from = 'name'

    # id is a UUID field that serves as the primary key for the Club model.
    # It is automatically generated and not editable.
    # This ensures that each club has a unique identifier.
    # UUIDField is used to generate a universally unique identifier for each club.
    # This is useful for ensuring that each club can be uniquely identified across the application.
    # The default value is set to uuid.uuid4(), which generates a new UUID each time a new club is created.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # name is a CharField that stores the name of the club.
    # It is required and cannot be blank.
    # The name field is not unique, allowing multiple clubs to have the same name.
    # This is useful for cases where clubs may share similar names or are located in different areas.
    # It is a CharField with a maximum length of 64 characters which is sufficient for most club names.
    # It is not allowed to be null or blank, ensuring that every club has a name.
    # The name field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their name or rebrand themselves.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("club name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the club.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple clubs to have the same slug.
    # This is useful for cases where multiple clubs may share the same name or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the club's name.
    # This allows for easy identification of the club in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # address is a CharField that stores the address of the club.
    # It is not required and can be blank.
    # The address field is not unique, allowing multiple clubs to have the same address.
    # This is useful for cases where clubs may share the same address or are located in the same area.
    # It is a CharField with a maximum length of 128 characters which is sufficient for most addresses.
    # It is allowed to be null or blank, meaning that clubs may not have a specific address associated with them
    # or prefer not to include it.
    # The address field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their address or provide it later.
    address = models.CharField(
        max_length=128,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("address of club"),
        help_text=_("format: not required, max-128")
    )

    # town is a CharField that stores the name of the town where the club is located.
    # It is not required and can be blank.
    # The town field is not unique, allowing multiple clubs to be located in the same town.
    # This is useful for cases where clubs may be located in the same area or region.
    # It is a CharField with a maximum length of 64 characters which is sufficient for most town names.
    # It is allowed to be null or blank, meaning that clubs may not have a specific town associated with them
    # or prefer not to include it.
    # The town field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their town name or provide it later.
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
    # The through argument specifies the Membership model as the intermediary model for this ManyToMany relationship.
    # The blank=True argument allows the archers field to be empty, meaning that a club can exist without any archers associated with it.
    # The related_name argument allows reverse access to the clubs associated with an archer.
    # This is useful for querying all clubs associated with a specific archer.
    # The archers field is not unique, allowing multiple clubs to have the same archers.
    # This is useful for cases where archers may be members of multiple clubs.
    # It is a ManyToManyField, which means it can store multiple relationships between clubs and archers.
    # The archers field is editable, allowing users to change the archers associated with a club if needed.
    # This is useful for cases where clubs may want to update their membership or add new archers.
    archers = models.ManyToManyField(
        Archer,
        through='Membership',
        blank=True,
        help_text=_("format: not required"),
        related_name='clubs',
        verbose_name=_("archers in club"),
    )

    # info is a TextField that stores additional information about the club.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple clubs to have the same information.
    # This is useful for cases where clubs may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that clubs may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their information or provide it later.
    # The info field is not required, allowing clubs to leave it blank if they do not have any additional information to provide.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("club information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the club to a User who created or manages the club's profile.
    # It uses PROTECT to prevent deletion of the user if there are clubs linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the clubs created by a user.
    # This is useful for querying all clubs associated with a specific user.
    # The author field is not unique, allowing multiple clubs to be created by the same user.
    # This is useful for cases where multiple clubs are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='author_club',
        verbose_name=_("author of club"),
        help_text=_("format: not required, default=1 (superuser)"),
    )

    # Extra fields for club information

    # email is an EmailField that stores the email address of the club.
    # It is not required and can be blank.
    # The email field is not unique, allowing multiple clubs to have the same email address.
    # This is useful for cases where clubs may not have a specific email address or prefer not to provide one.
    # It is an EmailField with a maximum length of 254 characters, which is sufficient for most email addresses.
    # It is allowed to be null or blank, meaning that clubs may not have an email address.
    # The email field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their email address or provide it later.
    # verbose_name provides a human-readable name for the field in the admin interface.
    # help_text provides additional information about the field's format and requirements.
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("email address of club"),
        help_text=_("format: not required, max-254")
    )

    # phone is a CharField that stores the phone number of the club.
    # It is not required and can be blank.
    # The phone field is not unique, allowing multiple clubs to have the same phone number.
    # This is useful for cases where clubs may not have a specific phone number or prefer not to provide one.
    # It is a CharField with a maximum length of 15 characters, which is sufficient for most phone numbers.
    # It is allowed to be null or blank, meaning that clubs may not have a phone number.
    # The phone field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their phone number or provide it later.
    # verbose_name provides a human-readable name for the field in the admin interface.
    # help_text provides additional information about the field's format and requirements.
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("phone number of club"),
        help_text=_("format: not required, max-15")
    )

    # website is a URLField that stores the website of the club.
    # It is not required and can be blank.
    # The website field is not unique, allowing multiple clubs to have the same website.
    # This is useful for cases where clubs may not have a specific website or prefer not to provide one.
    # It is a URLField with a maximum length of 200 characters, which is sufficient for most URLs.
    # It is allowed to be null or blank, meaning that clubs may not have a website.
    # The website field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their website or provide it later.
    # verbose_name provides a human-readable name for the field in the admin interface.
    # help_text provides additional information about the field's format and requirements.
    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("website of club"),
        help_text=_("format: not required, max-200")
    )

    # social_media is a CharField that stores the social media handle of the club.
    # It is not required and can be blank.
    # The social_media field is not unique, allowing multiple clubs to have the same social media handle.
    # This is useful for cases where clubs may not have a specific social media handle or prefer not to provide one.
    # It is a CharField with a maximum length of 128 characters, which is sufficient for most social media handles.
    # It is allowed to be null or blank, meaning that clubs may not have a social media handle.
    # The social_media field is editable, allowing users to change it if needed.
    # It is useful for cases where clubs may want to update their social media handle or provide it later.
    # verbose_name provides a human-readable name for the field in the admin interface.
    # help_text provides additional information about the field's format and requirements.
    social_media = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("social media handle of club"),
        help_text=_("format: not required, max-128")
    )
     
    # Extra fields for club information end        
    
    class Meta:
        """
        Meta options for the Club model.
        This model is used to represent an archery club in the application.
        The Meta class allows for customization of the model's behavior and appearance.
        It includes options such as the database table name, ordering, and verbose names.
        The Club model is used to store information about clubs, including their name, location,
        contact information, and relationships with archers.
        """

        # db_table specifies the name of the database table for this model.
        # This is useful for database management and migrations.
        # It allows for easy identification of the table associated with the Club model.
        # Using 'club' as the table name for clarity and consistency.
        # This is useful for database management and migrations.
        db_table = 'club'

        # Ordering by name for better readability in lists.
        # This ensures that when querying for clubs, they will be sorted by their name.
        # This is useful for displaying lists of clubs in a user-friendly manner.
        # The ordering can be overridden in queries if needed.
        # It is a good practice to order models by a field that is commonly used for identification.
        # Using 'name' as the field to order by for clarity and consistency.
        # This is useful for displaying lists of clubs in a user-friendly manner.
        ordering = ['name']

        # verbose_name is the singular name for the Club model.
        # This is used in the Django admin interface and other places where a singular name is needed.
        # It provides a human-readable name for the model.
        # Using "Club" as the singular name for clarity and consistency.
        # This is useful for displaying the club's name in a user-friendly manner.
        verbose_name = _("Club")

        # verbose_name_plural is the plural name for the Club model.
        # This is used in the Django admin interface and other places where a plural name is needed.
        # It provides a human-readable name for the model when referring to multiple instances.
        # Using "Clubs" as the plural name for clarity and consistency.
        # This is useful for displaying lists of clubs in a user-friendly manner.
        verbose_name_plural = _("Clubs")

    def __str__(self):
        """
        Return a string representation of the Club model.
        This method is used to provide a human-readable representation of the club's name.
        The string representation is useful for displaying the club's name in lists and other contexts.
        """

        return self.name

    def __unicode__(self):
        """
        Return a unicode representation of the Club model.
        This method is used to provide a human-readable representation of the club's name.
        The unicode representation is useful for displaying the club's name in lists and other contexts.
        """
        
        return self.name

class Membership(BaseModel):
    """
    Model representing a membership of an archer in a club.
    This model includes fields for membership information, relationships with clubs and archers,
    and additional details about the membership.
    It is designed to store information about memberships in the application.
    The Membership model inherits from BaseModel to include common fields for tracking creation and modification timestamps.
    The Membership model is used to represent a membership that an archer has in a club.
    It allows for tracking the relationship between archers and clubs, including start and end dates of the membership.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Membership model.
        This method is called when an instance of the Membership model is created.
        It allows for customization of the model's initialization process.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        # Call the parent class's __init__ method to ensure proper initialization.
        # This is necessary to ensure that the model is set up correctly.
        super().__init__(*args, **kwargs)
        
    # id is a UUID field that serves as the primary key for the Membership model.
    # It is automatically generated and not editable.
    # This ensures that each membership has a unique identifier.
    # UUIDField is used to generate a universally unique identifier for each membership.
    # This is useful for ensuring that each membership can be uniquely identified across the application.
    # The default value is set to uuid.uuid4(), which generates a new UUID each time a new membership is created.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # club is a ForeignKey that links the Membership model to the Club model.
    # It uses PROTECT to prevent deletion of the club if there are memberships linked to it.
    # The unique=False argument allows multiple memberships to be associated with the same club.
    # This is useful for cases where multiple archers can be members of the same club.
    # related_name allows reverse access to the memberships associated with a club.
    # This is useful for querying all memberships associated with a specific club.
    # The club field is not unique, allowing multiple memberships to be created for the same club.
    club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("club of the member"),
        help_text=_("format: required"),
        related_name='memberships'
    )

    # archer is a ForeignKey that links the Membership model to the Archer model.
    # It uses PROTECT to prevent deletion of the archer if there are memberships linked to them.
    # The unique=False argument allows multiple memberships to be associated with the same archer.
    # This is useful for cases where an archer can be a member of multiple clubs.
    # related_name allows reverse access to the memberships associated with an archer.
    # This is useful for querying all memberships associated with a specific archer.
    # The archer field is not unique, allowing multiple memberships to be created for the same archer.
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
    # The start_date field is not unique, allowing multiple memberships to have the same start date.
    # This is useful for cases where memberships may start on the same date.
    # It is a DateField, which means it stores dates in the format YYYY-MM-DD.
    # It is allowed to be null or blank, meaning that memberships may not have a specific start date.
    # This is useful for cases where memberships may not have a specific start date or prefer not to include it.
    # The start_date field is editable, allowing users to change it if needed.
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
    # The end_date field is not unique, allowing multiple memberships to have the same end date.
    # This is useful for cases where memberships may end on the same date.
    # It is a DateField, which means it stores dates in the format YYYY-MM-DD.
    # It is allowed to be null or blank, meaning that memberships may not have a specific end date.
    # This is useful for cases where memberships may not have a specific end date or prefer not to include it.
    # The end_date field is editable, allowing users to change it if needed.
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )
    
    # Extra fields for membership information
    
    # info is a TextField that stores additional information about the membership.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple memberships to have the same information.
    # This is useful for cases where memberships may have additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that memberships may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("membership information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the membership to a User who created or manages the membership.
    # It uses PROTECT to prevent deletion of the user if there are memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the memberships created by a user.
    # This is useful for querying all memberships associated with a specific user.
    # The author field is not unique, allowing multiple memberships to be created by the same user.
    # This is useful for cases where multiple memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='membership_author',
        verbose_name=_("author of membership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for membership information end

    class Meta:
        """
        Meta options for the Membership model.
        This model is used to represent a membership of an archer in a club.
        The Meta class allows for customization of the model's behavior and appearance.
        It includes options such as the database table name, ordering, and verbose names.
        The Membership model is used to store information about memberships, including the club, archer,
        start and end dates, and additional details about the membership.
        """

        # db_table specifies the name of the database table for this model.
        # This is useful for database management and migrations.
        # It allows for easy identification of the table associated with the Membership model.
        db_table = 'membership'

        # Ordering by start_date for better readability in lists.
        # This ensures that when querying for memberships, they will be sorted by their start date.
        # This is useful for displaying lists of memberships in a user-friendly manner.
        # The ordering can be overridden in queries if needed.
        ordering = ['start_date']

        # verbose_name is the singular name for the Membership model.
        # This is used in the Django admin interface and other places where a singular name is needed.
        # It provides a human-readable name for the model.
        verbose_name = _("Membership")

        # verbose_name_plural is the plural name for the Membership model.
        # This is used in the Django admin interface and other places where a plural name is needed.
        # It provides a human-readable name for the model when referring to multiple instances.
        verbose_name_plural = _("Memberships")

    def __str__(self):
        """
        Return a string representation of the Membership model.
        This method is used to provide a human-readable representation of the membership.
        The string representation is useful for displaying the membership in lists and other contexts.
        """

        # Use the string representation of the archer and club to create a meaningful description.
        # The string representation is useful for displaying the membership in lists and other contexts.
        # This allows for a more complete representation of the membership.
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

    def __unicode__(self):
        """
        Return a unicode representation of the Membership model.
        This method is used to provide a human-readable representation of the membership.
        The unicode representation is useful for displaying the membership in lists and other contexts.
        """

        # Use the string representation of the archer and club to create a meaningful description.
        # The unicode representation is useful for displaying the membership in lists and other contexts.
        # This allows for a more complete representation of the membership.
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

class Category(BaseModel):
    """
    Model representing a category of archers.
    This model includes fields for category information, relationships with archers,
    and additional details about the category.
    It is designed to store information about categories in the application.
    The Category model inherits from BaseModel to include common fields for tracking creation and modification timestamps.
    The Category model is used to represent a category that archers can belong to.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Category model and set up the slug field to be generated from the name field.
        This method is called when an instance of the Category model is created.
        It allows for customization of the model's initialization process.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        # Call the parent class's __init__ method to ensure proper initialization.
        # This is necessary to ensure that the model is set up correctly.
        # This allows the slug field to be automatically generated based on the name field.
        # The populate_from argument specifies that the slug should be generated from the name field.
        # This is useful for creating URL-friendly representations of the category.
        super().__init__(*args, **kwargs)
        self._meta.get_field('slug').populate_from = 'name'
        
    # id is a UUID field that serves as the primary key for the Category model.
    # It is automatically generated and not editable.
    # This ensures that each category has a unique identifier.
    # UUIDField is used to generate a universally unique identifier for each category.
    # This is useful for ensuring that each category can be uniquely identified across the application.
    # The default value is set to uuid.uuid4(), which generates a new UUID each time a new category is created.
    # This is usefule for database management and migrations.
    # It allows for easy identification of the table associated with the Category model.
    # The id field is not editable, meaning that it cannot be changed once after the category is created.    
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
    # The slug field is not unique, allowing multiple categories to have the same slug.
    # This is useful for cases where multiple categories may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the category's name.
    # This allows for easy identification of the category in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # archers is a ManyToManyField that links the Category model to the Archer model through the CategoryMembership model.
    # This allows multiple archers to be associated with a category and vice versa.
    # The through argument specifies the CategoryMembership model as the intermediary model for this ManyToMany relationship.
    # The blank=True argument allows the archers field to be empty, meaning that a category can exist without any archers associated with it.
    # The related_name argument allows reverse access to the categories associated with an archer.
    # This is useful for querying all categories associated with a specific archer.
    # The archers field is not unique, allowing multiple categories to have the same archers.
    # This is useful for cases where archers may belong to multiple categories.
    # It is a ManyToManyField, which means it can store multiple relationships between categories and archers.
    # The archers field is editable, allowing users to change the archers associated with a category if needed.
    # This is useful for cases where categories may want to update their membership or add new archers.
    archers = models.ManyToManyField(
        Archer,
        through='CategoryMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='categories',
        verbose_name=_("archers in category"),
    )
    
    # info is a TextField that stores additional information about the category.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple categories to have the same information.
    # This is useful for cases where categories may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that categories may not have additional information.
    # The  info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("category information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the category to a User who created or manages the category's profile.
    # It uses PROTECT to prevent deletion of the user if there are categories linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the categories created by a user.
    # This is useful for querying all categories associated with a specific user.
    # The author field is not unique, allowing multiple categories to be created by the same user.
    # This is useful for cases where multiple categories are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='category_author',
        verbose_name=_("author of category"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for category information
    # age_group is a CharField that stores the age group of the category.
    # It is not required and can be blank.
    # The age_group field is not unique, allowing multiple categories to have the same age group.
    # This is useful for cases where categories may share the same age group or are located in different areas.
    # It is a CharField with a maximum length of 32 characters which is sufficient for most age group names.
    # It is allowed to be null or blank, meaning that categories may not have a specific age group associated with them
    # or prefer not to include it.
    # The age_group field is editable, allowing users to change it if needed.
    # It is useful for cases where categories may want to update their age group or provide it later.
    age_group = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("age group of category"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("youth", "Youth"),
            ("junior", "Junior"),
            ("senior", "Senior"),
            ("master", "Master"),
            ("veteran", "Veteran"),
            ("other", "Other")
        ]
    )
    
    # age_group end
    
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the bow type.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple bow types to have the same slug.
    # This is useful for cases where multiple bow types may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the bow type's name.
    # This allows for easy identification of the bow type in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='bowtypes'
    )

    # info is a TextField that stores additional information about the bow type.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple bow types to have the same information.
    # This is useful for cases where bow types may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that bow types may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bow type information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the bow type to a User who created or manages the bow type's profile.
    # It uses PROTECT to prevent deletion of the user if there are bow types linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow types created by a user.
    # This is useful for querying all bow types associated with a specific user.
    # The author field is not unique, allowing multiple bow types to be created by the same user.
    # This is useful for cases where multiple bow types are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowtype_author',
        verbose_name=_("author of bow type"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the bow string.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple bow strings to have the same slug.
    # This is useful for cases where multiple bow strings may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the bow string's name.
    # This allows for easy identification of the bow string in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowstring bowtype"),
        help_text=_("format: required"),
        related_name='bowstrings'
    )

    # info is a TextField that stores additional information about the bow string.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple bow strings to have the same information.
    # This is useful for cases where bow strings may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that bow strings may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowstring information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the bow string to a User who created or manages the bow string's profile.
    # It uses PROTECT to prevent deletion of the user if there are bow strings linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow strings created by a user.
    # This is useful for querying all bow strings associated with a specific user.
    # The author field is not unique, allowing multiple bow strings to be created by the same user.
    # This is useful for cases where multiple bow strings are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowstring_author',
        verbose_name=_("author of bow string"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the bow riser.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple bow risers to have the same slug.
    # This is useful for cases where multiple bow risers may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the bow riser's name.
    # This allows for easy identification of the bow riser in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowriser bowtype"),
        help_text=_("format: required"),
        related_name='bowrisers'
    )

    # info is a TextField that stores additional information about the bow riser.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple bow risers to have the same information.
    # This is useful for cases where bow risers may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that bow risers may not have additional information.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowriser information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the bow riser to a User who created or manages the bow riser's profile.
    # It uses PROTECT to prevent deletion of the user if there are bow risers linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow risers created by a user.
    # This is useful for querying all bow risers associated with a specific user.
    # The author field is not unique, allowing multiple bow risers to be created by the same user.
    # This is useful for cases where multiple bow risers are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowriser_author',
        verbose_name=_("author of bow riser"),
        help_text=_("format: required, default=1 (superuser)"),
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

class BowRiserMembership(BaseModel):
    """
    Model representing the relationship between a bow riser and an archer.
    This model is used to track which bow risers are used by which archers.
    """

    # id is a UUID field that serves as the primary key for the BowRiserMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bowriser is a foreign key to the BowRiser model, indicating which bow riser is being used by the archer.
    bowriser = models.ForeignKey(
        BowRiser,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowrisermembership bowriser"),
        help_text=_("format: required"),
        related_name='bowrisermemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is using the bow riser.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowrisermembership archer"),
        help_text=_("format: required"),
        related_name='bowrisermembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the bow riser membership.
    # It uses PROTECT to prevent deletion of the user if there are bow riser memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow riser memberships created by a user.
    # This is useful for querying all bow riser memberships associated with a specific user.
    # The author field is not unique, allowing multiple bow riser memberships to be created by the same user.
    # This is useful for cases where multiple bow riser memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowrisermembership_author',
        verbose_name=_("author of bow riser membership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the BowRiserMembership model.
        verbose_name = _("Bow Riser Membership")
        # verbose_name_plural is the plural name for the BowRiserMembership model.
        verbose_name_plural = _("Bow Riser Memberships")

    def __str__(self):
        """
        Returns a string representation of the BowRiserMembership instance.
        This representation includes the archer and bow riser names.
        """
        return f"{str(self.archer)} - {str(self.bowriser)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the BowRiserMembership instance.
        This representation includes the archer and bow riser names.
        """
        return f"{str(self.archer)} - {str(self.bowriser)}"

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

    # slug is an AutoSlugField that automatically generates a slug from the name of the bow limb.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple bow limbs to have the same slug.
    # This is useful for cases where multiple bow limbs may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the bow limb's name.
    # This allows for easy identification of the bow limb in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowlimb bowtype"),
        help_text=_("format: required"),
        related_name='bowlimbs'
    )

    # info is a TextField that stores additional information about the bow limb.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple bow limbs to have the same information.
    # This is useful for cases where bow limbs may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that bow limbs may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowlimb information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the bow limb to a User who created or manages the bow limb's profile.
    # It uses PROTECT to prevent deletion of the user if there are bow limbs linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow limbs created by a user.
    # This is useful for querying all bow limbs associated with a specific user.
    # The author field is not unique, allowing multiple bow limbs to be created by the same user.
    # This is useful for cases where multiple bow limbs are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowlimb_author',
        verbose_name=_("author of bow limb"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the team.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple teams to have the same slug.
    # This is useful for cases where multiple teams may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the team's name.
    # This allows for easy identification of the team in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    '''archer is a many-to-many relationship with the Archer model, allowing multiple archers to be part of a team.'''
    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='teams'
    )

    # info is a TextField that stores additional information about the team.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple teams to have the same information.
    # This is useful for cases where teams may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that teams may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("team information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the team to a User who created or manages the team's profile.
    # It uses PROTECT to prevent deletion of the user if there are teams linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the teams created by a user.
    # This is useful for querying all teams associated with a specific user.
    # The author field is not unique, allowing multiple teams to be created by the same user.
    # This is useful for cases where multiple teams are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='team_author',
        verbose_name=_("author of team"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the contest.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple contests to have the same slug.
    # This is useful for cases where multiple contests may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the contest's name.
    # This allows for easy identification of the contest in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='contests'
    )

    # info is a TextField that stores additional information about the contest.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple contests to have the same information.
    # This is useful for cases where contests may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that contests may not have additional information.
    # The info field is editable, allowing users to change it if needed.
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
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end date of contest"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_time = models.TimeField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end time of contest"),
        help_text=_("format: H:M:S, not required"),
    )
    location = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("contest location"),
        help_text=_("format: not required, max-128"),
    )
    targetface = models.ForeignKey(
        "TargetFace",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("targetface used in contest"),
        help_text=_("format: not required"),
        related_name='contest_targetface'
    )
    scoringsheet = models.ForeignKey(
        "ScoringSheet",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("scoringsheet used in contest"),
        help_text=_("format: not required"),
        related_name='contest_scoringsheet'
    )

    # author is a ForeignKey that links the contest to a User who created or manages the contest's profile.
    # It uses PROTECT to prevent deletion of the user if there are contests linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the contests created by a user.
    # This is useful for querying all contests associated with a specific user.
    # The author field is not unique, allowing multiple contests to be created by the same user.
    # This is useful for cases where multiple contests are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='contest_author',
        verbose_name=_("author of contest"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the target face.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple target faces to have the same slug.
    # This is useful for cases where multiple target faces may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the target face's name.
    # This allows for easy identification of the target face in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
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

    # info is a TextField that stores additional information about the target face.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple target faces to have the same information.
    # This is useful for cases where target faces may want to provide additional details or descriptions.
    # It is a text field, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that target faces may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("targetface information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the target face to a User who created or manages the target face's profile.
    # It uses PROTECT to prevent deletion of the user if there are target faces linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the target faces created by a user.
    # This is useful for querying all target faces associated with a specific user.
    # The author field is not unique, allowing multiple target faces to be created by the same user.
    # This is useful for cases where multiple target faces are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='targetface_author',
        verbose_name=_("author of target face"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the scoring sheet.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple scoring sheets to have the same slug.
    # This is useful for cases where multiple scoring sheets may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the scoring sheet's name.
    # This allows for easy identification of the scoring sheet in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
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

    # info is a TextField that stores additional information about the scoring sheet.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple scoring sheets to have the same information.
    # This is useful for cases where scoring sheets may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that scoring sheets may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("scoringsheet information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the scoring sheet to a User who created or manages the scoring sheet's profile.
    # It uses PROTECT to prevent deletion of the user if there are scoring sheets linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the scoring sheets created by a user.
    # This is useful for querying all scoring sheets associated with a specific user.
    # The author field is not unique, allowing multiple scoring sheets to be created by the same user.
    # This is useful for cases where multiple scoring sheets are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='scoringsheet_author',
        verbose_name=_("author of scoring sheet"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the score.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple results to have the same slug.
    # This is useful for cases where multiple results may share similar scores or are located in different areas.
    # The slug is generated from the score field, ensuring that it is always based on the result's score.
    # This allows for easy identification of the result in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
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

    # info is a TextField that stores additional information about the result.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple results to have the same information.
    # This is useful for cases where results may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that results may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("result information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the result to a User who created or manages the result's profile.
    # It uses PROTECT to prevent deletion of the user if there are results linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the results created by a user.
    # This is useful for querying all results associated with a specific user.
    # The author field is not unique, allowing multiple results to be created by the same user.
    # This is useful for cases where multiple results are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='result_author',
        verbose_name=_("author of result"),
        help_text=_("format: required, default=1 (superuser)"),
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

class ResultMembership(BaseModel):
    """
    Model representing the relationship between an archer and a score.
    This model is used to track which archers have achieved which scores.
    """

    # id is a UUID field that serves as the primary key for the ScoreMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # archer is a foreign key to the Archer model, indicating which archer achieved the score.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("scoremembership archer"),
        help_text=_("format: required"),
        related_name='scorememberships'
    )
    # score is a foreign key to the Score model, indicating which score is being associated with the archer.
    score = models.ForeignKey(
        "Score",
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("scoremembership score"),
        help_text=_("format: required"),
        related_name='scoremembership_score'
    )

    class Meta:
       verbose_name = _("Score Membership")
       verbose_name_plural = _("Score Memberships")

    def __str__(self):
       """
       Returns a string representation of the ScoreMembership instance.
       This representation includes the archer and score details.
       """
       return f"{str(self.archer)} - {str(self.score)}"
    def __unicode__(self):
       """
       Returns a unicode representation of the ScoreMembership instance.
       This representation includes the archer and score details.
       """
       return f"{str(self.archer)} - {str(self.score)}"

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

    # slug is an AutoSlugField that automatically generates a slug from the name of the competition.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple competitions to have the same slug.
    # This is useful for cases where multiple competitions may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the competition's name.
    # This allows for easy identification of the competition in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    archer = models.ManyToManyField(
        Archer,
        blank=True,
        help_text=_("format: not required"),
        related_name='competitions'
    )

    # info is a TextField that stores additional information about the competition.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple competitions to have the same information.
    # This is useful for cases where competitions may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that competitions may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("competition information"),
        help_text=_("format: not required"),
    )

    # Extra fields
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start date of competition"),
        help_text=_("format: Y-m-d, not required"),
    )
    start_time = models.TimeField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start time of competition"),
        help_text=_("format: H:M:S, not required"),
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end date of competition"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_time = models.TimeField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end time of competition"),
        help_text=_("format: H:M:S, not required"),
    )
    location = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("competition location"),
        help_text=_("format: not required, max-128"),
    )
    targetface = models.ForeignKey(
        "TargetFace",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("targetface used in competition"),
        related_name='competition_targetface',
        help_text=_("format: not required"),
    )
    scoringsheet = models.ForeignKey(
        "ScoringSheet",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("scoringsheet used in competition"),
        related_name='competition_scoringsheet',
        help_text=_("format: not required"),
    )

    # Extra fields end

    # author is a ForeignKey that links the competition to a User who created or manages the competition's profile.
    # It uses PROTECT to prevent deletion of the user if there are competitions linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the competitions created by a user.
    # This is useful for querying all competitions associated with a specific user.
    # The author field is not unique, allowing multiple competitions to be created by the same user.
    # This is useful for cases where multiple competitions are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='competition_author',
        verbose_name=_("author of competition"),
        help_text=_("format: required, default=1 (superuser)"),
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

    # slug is an AutoSlugField that automatically generates a slug from the name of the arrow.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple arrows to have the same slug.
    # This is useful for cases where multiple arrows may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the arrow's name.
    # This allows for easy identification of the arrow in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a TextField that stores additional information about the arrow.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple arrows to have the same information.
    # This is useful for cases where arrows may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that arrows may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("arrow information"),
        help_text=_("format: not required"),
    )

    # author is a ForeignKey that links the arrow to a User who created or manages the arrow's profile.
    # It uses PROTECT to prevent deletion of the user if there are arrows linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the arrows created by a user.
    # This is useful for querying all arrows associated with a specific user.
    # The author field is not unique, allowing multiple arrows to be created by the same user.
    # This is useful for cases where multiple arrows are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='arrow_author',
        verbose_name=_("author of arrow"),
        help_text=_("format: required, default=1 (superuser)"),
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

class ArrowType(BaseModel):
    """
    Model representing an arrow type used in archery.
    """

    # id is a UUID field that serves as the primary key for the ArrowType model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the arrow type, which describes the type of arrow.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("arrow type name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the arrow type.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple arrow types to have the same slug.
    # This is useful for cases where multiple arrow types may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the arrow type's name.
    # This allows for easy identification of the arrow type in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a text field for additional information about the arrow type.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple arrow types to have the same information.
    # This is useful for cases where arrow types may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that arrow types may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("arrow type information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the arrow type.
    # It uses PROTECT to prevent deletion of the user if there are arrow types linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the arrow types created by a user.
    # This is useful for querying all arrow types associated with a specific user.
    # The author field is not unique, allowing multiple arrow types to be created by the same user.
    # This is useful for cases where multiple arrow types are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='arrowtype_author',
        verbose_name=_("author of arrow type"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Specific fields

    class Meta:
       verbose_name = _("Arrow Type")
       verbose_name_plural = _("Arrow Types")
    def __str__(self):
       return self.name
    def __unicode__(self):
       return self.name

class ArrowTypeMembership(BaseModel):
    """
    Model representing the relationship between an arrow and its type.
    """

    # id is a UUID field that serves as the primary key for the ArrowTypeMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # arrow is a foreign key to the Arrow model, indicating which arrow is being associated with the type.
    arrow = models.ForeignKey(
        Arrow,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("arrowtypemembership arrow"),
        help_text=_("format: required"),
        related_name='arrowtypememberships'
    )
    # arrowtype is a foreign key to the ArrowType model, indicating which type of arrow is being used.
    arrowtype = models.ForeignKey(
        ArrowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("arrowtypemembership arrowtype"),
        help_text=_("format: required"),
        related_name='arrowtypemembership_arrowtype'
    )

    # author is a foreign key to the User model, indicating who created the arrow type membership.
    # It uses PROTECT to prevent deletion of the user if there are arrow type memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the arrow type memberships created by a user.
    # This is useful for querying all arrow type memberships associated with a specific user.
    # The author field is not unique, allowing multiple arrow type memberships to be created by the same user.
    # This is useful for cases where multiple arrow type memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of arrow type membership"),
        related_name='arrowtypemembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    class Meta:
        # verbose_name is the singular name for the ArrowTypeMembership model.
        verbose_name = _("Arrow Type Membership")
        # verbose_name_plural is the plural name for the ArrowTypeMembership model.
        verbose_name_plural = _("Arrow Type Memberships")
    def __str__(self):
        """
        Returns a string representation of the ArrowTypeMembership instance.
        This representation includes the arrow and arrow type names.
        """
        return f"{str(self.arrow)} - {str(self.arrowtype)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the ArrowTypeMembership instance.
        This representation includes the arrow and arrow type names.
        """
        return f"{str(self.arrow)} - {str(self.arrowtype)}"

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

    # slug is an AutoSlugField that automatically generates a slug from the name of the fletching.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple fletchings to have the same slug.
    # This is useful for cases where multiple fletchings may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the fletching's name.
    # This allows for easy identification of the fletching in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)
    
    # arrow is a many-to-many relationship with the Arrow model, allowing multiple arrows to be associated with a fletching.
    arrow = models.ManyToManyField(
        Arrow,
        blank=True,
        help_text=_("format: not required"),
        related_name='fletchings'
    )

    # info is a text field for additional information about the fletching.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple fletchings to have the same information.
    # This is useful for cases where fletchings may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that fletchings may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("fletching information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the fletching.
    # It uses PROTECT to prevent deletion of the user if there are fletchings linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the fletchings created by a user.
    # This is useful for querying all fletchings associated with a specific user.
    # The author field is not unique, allowing multiple fletchings to be created by the same user.
    # This is useful for cases where multiple fletchings are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of fletching"),
        related_name='fletching_author',
        help_text=_("format: required, default=1 (superuser)"),
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
    # It uses PROTECT to prevent deletion of the user if there are arrow fletchings linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the arrow fletchings created by a user.
    # This is useful for querying all arrow fletchings associated with a specific user.
    # The author field is not unique, allowing multiple arrow fletchings to be created by the same user.
    # This is useful for cases where multiple arrow fletchings are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of arrow fletching"),
        related_name='arrowfletching_author',
        help_text=_("format: required, default=1 (superuser)"),
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

class BowSight(BaseModel):
    """
    Model representing a bow sight used in archery.
    """

    # id is a UUID field that serves as the primary key for the BowSight model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the bow sight.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("bow sight name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the bow sight.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple bow sights to have the same slug.
    # This is useful for cases where multiple bow sights may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the bow sight's name.
    # This allows for easy identification of the bow sight in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # bowtype is a foreign key to the BowType model, indicating which type of bow the sight is compatible with.
    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsight bowtype"),
        help_text=_("format: required"),
        related_name='bowsights'
    )

    # info is a text field for additional information about the bow sight.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple bow sights to have the same information.
    # This is useful for cases where bow sights may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that bow sights may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowsight information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the bow sight.
    # It uses PROTECT to prevent deletion of the user if there are bow sights linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow sights created by a user.
    # This is useful for querying all bow sights associated with a specific user.
    # The author field is not unique, allowing multiple bow sights to be created by the same user.
    # This is useful for cases where multiple bow sights are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow sight"),
        related_name='bowsight_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Specific fields
    # Sight type indicates whether the sight is a fixed pin sight, adjustable sight, or other types.
    sight_type = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowsight type"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("fixed_pin", "Fixed Pin"),
            ("adjustable", "Adjustable"),
            ("other", "Other")
        ]
    )
    # Sight color is the color of the sight, which can affect visibility and aesthetics.
    color = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowsight color"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("black", "Black"),
            ("red", "Red"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("yellow", "Yellow"),
            ("other", "Other")
        ]
    )
    # Sight material is the type of material used for the sight, which can affect durability and weight.
    material = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name=_("bowsight material"),
        help_text=_("format: not required, max-32"),
        choices=[
            ("aluminum", "Aluminum"),
            ("carbon", "Carbon"),
            ("plastic", "Plastic"),
            ("other", "Other")
        ]
    )
    # Sight length is the length of the sight, which can affect visibility and adjustability.
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowsight length in inches"),
        help_text=_("format: not required"),
    )
    # Sight weight is the weight of the sight, which can affect overall bow balance and handling.
    weight = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("bowsight weight in grams"),
        help_text=_("format: not required"),
    )

    class Meta:
       verbose_name = _("Bow Sight")
       verbose_name_plural = _("Bow Sights")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class BowSightArcher(BaseModel):
    """
    Model representing the relationship between an archer and a bow sight.
    """

    # id is a UUID field that serves as the primary key for the BowSightArcher model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bowsight is a foreign key to the BowSight model, indicating which bow sight is being used by the archer.
    bowsight = models.ForeignKey(
        BowSight,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsightarcher bowsight"),
        help_text=_("format: required"),
        related_name='bowsightarchers'
    )
    # archer is a foreign key to the Archer model, indicating which archer is using the bow sight.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsightarcher archer"),
        help_text=_("format: required"),
        related_name='bowsightarcher_archer'
    )

    # author is a foreign key to the User model, indicating who created the bow sight archer relationship.
    # It uses PROTECT to prevent deletion of the user if there are bow sight archers linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow sight archers created by a user.
    # This is useful for querying all bow sight archers associated with a specific user.
    # The author field is not unique, allowing multiple bow sight archers to be created by the same user.
    # This is useful for cases where multiple bow sight archers are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bowsight archer"),
        related_name='bowsightarcher_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    class Meta:
        # verbose_name is the singular name for the BowSightArcher model.
        verbose_name = _("Bow Sight Archer")
        # verbose_name_plural is the plural name for the BowSightArcher model.
        verbose_name_plural = _("Bow Sight Archers")
    def __str__(self):
        """
        Returns a string representation of the BowSightArcher instance.
        This representation includes the archer and bow sight names.
        """
        return f"{str(self.archer)} - {str(self.bowsight)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the BowSightArcher instance.
        This representation includes the archer and bow sight names.
        """
        return f"{str(self.archer)} - {str(self.bowsight)}"

class Round(BaseModel):
    """
    Model representing a round in archery, which is a specific set of shooting distances and target faces.
    """

    # id is a UUID field that serves as the primary key for the Round model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the round, which describes the round type.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("round name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the round.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple rounds to have the same slug.
    # This is useful for cases where multiple rounds may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the round's name.
    # This allows for easy identification of the round in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # targetface is a foreign key to the TargetFace model, indicating which target face is used in this round.
    targetface = models.ForeignKey(
        TargetFace,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("round targetface"),
        help_text=_("format: required"),
        related_name='rounds'
    )
    # distance is a positive integer field indicating the shooting distance in meters for this round.
    distance = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("round distance in meters"),
        help_text=_("format: required"),
    )

    # info is a text field for additional information about the round.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple rounds to have the same information.
    # This is useful for cases where rounds may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that rounds may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("round information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the round.
    # It uses PROTECT to prevent deletion of the user if there are rounds linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the rounds created by a user.
    # This is useful for querying all rounds associated with a specific user.
    # The author field is not unique, allowing multiple rounds to be created by the same user.
    # This is useful for cases where multiple rounds are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of round"),
        related_name='round_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
       verbose_name = _("Round")
       verbose_name_plural = _("Rounds")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class RoundMembership(BaseModel):
    """
    Model representing the relationship between a round and an archer.
    """

    # id is a UUID field that serves as the primary key for the RoundMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # round is a foreign key to the Round model, indicating which round is being participated in.
    round = models.ForeignKey(
        Round,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("roundmembership round"),
        help_text=_("format: required"),
        related_name='roundmemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is participating in the round.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("roundmembership archer"),
        help_text=_("format: required"),
        related_name='roundmembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the round membership.
    # It uses PROTECT to prevent deletion of the user if there are round memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the round memberships created by a user.
    # This is useful for querying all round memberships associated with a specific user.
    # The author field is not unique, allowing multiple round memberships to be created by the same user.
    # This is useful for cases where multiple round memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of round membership"),
        related_name='roundmembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the RoundMembership model.
        verbose_name = _("Round Membership")
        # verbose_name_plural is the plural name for the RoundMembership model.
        verbose_name_plural = _("Round Memberships")
    def __str__(self):
        """
        Returns a string representation of the RoundMembership instance.
        This representation includes the archer and round names.
        """
        return f"{str(self.archer)} - {str(self.round)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the RoundMembership instance.
        This representation includes the archer and round names.
        """
        return f"{str(self.archer)} - {str(self.round)}"

class Distance(BaseModel):
    """
    Model representing a distance used in archery rounds.
    """

    # id is a UUID field that serves as the primary key for the Distance model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the distance, which describes the distance type.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("distance name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the distance.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple distances to have the same slug.
    # This is useful for cases where multiple distances may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the distance's name.
    # This allows for easy identification of the distance in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a text field for additional information about the distance.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple distances to have the same information.
    # This is useful for cases where distances may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that distances may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("distance information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the distance.
    # It uses PROTECT to prevent deletion of the user if there are distances linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the distances created by a user.
    # This is useful for querying all distances associated with a specific user.
    # The author field is not unique, allowing multiple distances to be created by the same user.
    # This is useful for cases where multiple distances are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of distance"),
        related_name='distance_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
       verbose_name = _("Distance")
       verbose_name_plural = _("Distances")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name
    
class RoundDistance(BaseModel):
    """
    Model representing the relationship between a round and a distance.
    """

    # id is a UUID field that serves as the primary key for the RoundDistance model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # round is a foreign key to the Round model, indicating which round is being associated with the distance.
    round = models.ForeignKey(
        Round,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("rounddistance round"),
        help_text=_("format: required"),
        related_name='rounddistances'
    )
    # distance is a foreign key to the Distance model, indicating which distance is being used in the round.
    distance = models.ForeignKey(
        Distance,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("rounddistance distance"),
        help_text=_("format: required"),
        related_name='rounddistance_distance'
    )
    # author is a foreign key to the User model, indicating who created the round distance relationship.
    # It uses PROTECT to prevent deletion of the user if there are round distances linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the round distances created by a user.
    # This is useful for querying all round distances associated with a specific user.
    # The author field is not unique, allowing multiple round distances to be created by the same user.
    # This is useful for cases where multiple round distances are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of round distance"),
        related_name='rounddistance_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields can be added here if needed, such as:

    class Meta:
        # verbose_name is the singular name for the RoundDistance model.
        verbose_name = _("Round Distance")
        # verbose_name_plural is the plural name for the RoundDistance model.
        verbose_name_plural = _("Round Distances")

    def __str__(self):
        """
        Returns a string representation of the RoundDistance instance.
        This representation includes the round and distance names.
        """
        return f"{str(self.round)} - {str(self.distance)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the RoundDistance instance.
        This representation includes the round and distance names.
        """
        return f"{str(self.round)} - {str(self.distance)}"

class Range(BaseModel):
    """
    Model representing a range used for archery shooting.
    """

    # id is a UUID field that serves as the primary key for the Range model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the range, which describes the range type.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("range name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the range.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple ranges to have the same slug.
    # This is useful for cases where multiple ranges may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the range's name.
    # This allows for easy identification of the range in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a text field for additional information about the range.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple ranges to have the same information.
    # This is useful for cases where ranges may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that ranges may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("range information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the range.
    # It uses PROTECT to prevent deletion of the user if there are ranges linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the ranges created by a user.
    # This is useful for querying all ranges associated with a specific user.
    # The author field is not unique, allowing multiple ranges to be created by the same user.
    # This is useful for cases where multiple ranges are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of range"),
        related_name='range_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
       verbose_name = _("Range")
       verbose_name_plural = _("Ranges")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name
    
class RangeRound(BaseModel):
    """
    Model representing the relationship between a range and a round.
    """

    # id is a UUID field that serves as the primary key for the RangeRound model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # range is a foreign key to the Range model, indicating which range is being associated with the round.
    range = models.ForeignKey(
        Range,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("rangeround range"),
        help_text=_("format: required"),
        related_name='rangerounds'
    )
    # round is a foreign key to the Round model, indicating which round is being used at the range.
    round = models.ForeignKey(
        Round,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("rangeround round"),
        help_text=_("format: required"),
        related_name='rangeround_round'
    )

    # author is a foreign key to the User model, indicating who created the range round relationship.
    # It uses PROTECT to prevent deletion of the user if there are range rounds linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the range rounds created by a user.
    # This is useful for querying all range rounds associated with a specific user.
    # The author field is not unique, allowing multiple range rounds to be created by the same user.
    # This is useful for cases where multiple range rounds are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of range round"),
        related_name='rangeround_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    class Meta:
        # verbose_name is the singular name for the RangeRound model.
        verbose_name = _("Range Round")
        # verbose_name_plural is the plural name for the RangeRound model.
        verbose_name_plural = _("Range Rounds")
    def __str__(self):
        """ Returns a string representation of the RangeRound instance.
        This representation includes the range and round names.
        """
        return f"{str(self.range)} - {str(self.round)}"
    def __unicode__(self):
        """ Returns a unicode representation of the RangeRound instance.
        This representation includes the range and round names.
        """
        return f"{str(self.range)} - {str(self.round)}"

class Score(BaseModel):
    """
    Model representing a score in an archery round.
    """

    # id is a UUID field that serves as the primary key for the Score model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # archer is a foreign key to the Archer model, indicating which archer scored the points.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("score archer"),
        help_text=_("format: required"),
        related_name='scores'
    )
    # round is a foreign key to the Round model, indicating which round the score belongs to.
    round = models.ForeignKey(
        Round,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("score round"),
        help_text=_("format: required"),
        related_name='scores'
    )
    # score is a positive integer field indicating the number of points scored by the archer.
    score = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("score points"),
        help_text=_("format: required"),
    )
    arrows = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("archerscore arrows"),
        help_text=_("format: not required"),
    )

    class Meta:
       verbose_name = _("Score")
       verbose_name_plural = _("Scores")

    def __str__(self):
       return f"{self.archer} - {self.round} - {self.score}"

    def __unicode__(self):
       return f"{self.archer} - {self.round} - {self.score}"

class ScoreMembership(BaseModel):
    """
    Model representing the relationship between an archer and a score.
    This model is used to associate a score with an archer, allowing for tracking of scores achieved by each archer.
    """

    # id is a UUID field that serves as the primary key for the ScoreMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # score is a foreign key to the Score model, indicating which score is being associated with the archer.
    score = models.ForeignKey(
        Score,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("scoremembership score"),
        help_text=_("format: required"),
        related_name='scorememberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer achieved the score.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("scoremembership archer"),
        help_text=_("format: required"),
        related_name='scoremembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the score membership.
    # It uses PROTECT to prevent deletion of the user if there are score memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the score memberships created by a user.
    # This is useful for querying all score memberships associated with a specific user.
    # The author field is not unique, allowing multiple score memberships to be created by the same user.
    # This is useful for cases where multiple score memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of score membership"),
        related_name='scoremembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the ScoreMembership model.
        verbose_name = _("Score Membership")
        # verbose_name_plural is the plural name for the ScoreMembership model.
        verbose_name_plural = _("Score Memberships")

    def __str__(self):
        """
        Returns a string representation of the ScoreMembership instance.
        This representation includes the archer and score details.
        """
        return f"{str(self.archer)} - {str(self.score)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the ScoreMembership instance.
        This representation includes the archer and score details.
        """
        return f"{str(self.archer)} - {str(self.score)}"

class CompetitionScore(BaseModel):
    """
    Model representing a score in a competition.
    """

    # id is a UUID field that serves as the primary key for the CompetitionScore model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # competition is a foreign key to the Competition model, indicating which competition the score belongs to.
    competition = models.ForeignKey(
        Competition,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("competitionscore competition"),
        help_text=_("format: required"),
        related_name='competitionscores'
    )
    # archer is a foreign key to the Archer model, indicating which archer achieved the score.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("competitionscore archer"),
        help_text=_("format: required"),
        related_name='competitionscore_archer'
    )
    # score is a positive integer field indicating the number of points scored by the archer in the competition.
    score = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("competitionscore points"),
        help_text=_("format: required"),
    )

    class Meta:
       verbose_name = _("Competition Score")
       verbose_name_plural = _("Competition Scores")

    def __str__(self):
       return f"{self.competition} - {self.archer} - {self.score}"

    def __unicode__(self):
       return f"{self.competition} - {self.archer} - {self.score}"

class ClubChampionship(BaseModel):
    """
    Model representing a club championship, which is a competition within a club.
    """

    # id is a UUID field that serves as the primary key for the ClubChampionship model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the club championship, which describes the championship type.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("club championship name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the club championship.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple club championships to have the same slug.
    # This is useful for cases where multiple club championships may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the club championship's name.
    # This allows for easy identification of the club championship in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a text field for additional information about the club championship.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple club championships to have the same information.
    # This is useful for cases where club championships may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that club championships may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("club championship information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the club championship.
    # It uses PROTECT to prevent deletion of the user if there are club championships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the club championships created by a user.
    # This is useful for querying all club championships associated with a specific user.
    # The author field is not unique, allowing multiple club championships to be created by the same user.
    # This is useful for cases where multiple club championships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of club championship"),
        related_name='clubchampionship_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
       verbose_name = _("Club Championship")
       verbose_name_plural = _("Club Championships")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class ClubChampionshipMembership(BaseModel):
    """
    Model representing the relationship between a club championship and an archer.
    """

    # id is a UUID field that serves as the primary key for the ClubChampionshipMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # clubchampionship is a foreign key to the ClubChampionship model, indicating which championship is being participated in.
    clubchampionship = models.ForeignKey(
        ClubChampionship,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("clubchampionshipmembership clubchampionship"),
        help_text=_("format: required"),
        related_name='clubchampionshipmemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is participating in the club championship.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("clubchampionshipmembership archer"),
        help_text=_("format: required"),
        related_name='clubchampionshipmembership_archer'
    )
    
    # author is a foreign key to the User model, indicating who created the club championship membership.
    # It uses PROTECT to prevent deletion of the user if there are club championship memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the club championship memberships created by a user.
    # This is useful for querying all club championship memberships associated with a specific user.
    # The author field is not unique, allowing multiple club championship memberships to be created by the same user.
    # This is useful for cases where multiple club championship memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of club championship membership"),
        related_name='clubchampionshipmembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    class Meta:
        # verbose_name is the singular name for the ClubChampionshipMembership model.
        verbose_name = _("Club Championship Membership")
        # verbose_name_plural is the plural name for the ClubChampionshipMembership model.
        verbose_name_plural = _("Club Championship Memberships")
    def __str__(self):
        """
        Returns a string representation of the ClubChampionshipMembership instance.
        This representation includes the archer and club championship names.
        """
        return f"{str(self.archer)} - {str(self.clubchampionship)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the ClubChampionshipMembership instance.
        This representation includes the archer and club championship names.
        """
        return f"{str(self.archer)} - {str(self.clubchampionship)}"

class ClubChampionshipScore(BaseModel):
    """
    Model representing a score in a club championship.
    """

    # id is a UUID field that serves as the primary key for the ClubChampionshipScore model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # clubchampionship is a foreign key to the ClubChampionship model, indicating which championship the score belongs to.
    clubchampionship = models.ForeignKey(
        ClubChampionship,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("clubchampionshipscore clubchampionship"),
        help_text=_("format: required"),
        related_name='clubchampionshipscores'
    )
    # archer is a foreign key to the Archer model, indicating which archer achieved the score.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("clubchampionshipscore archer"),
        help_text=_("format: required"),
        related_name='clubchampionshipscore_archer'
    )
    # score is a positive integer field indicating the number of points scored by the archer in the club championship.
    score = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("clubchampionshipscore points"),
        help_text=_("format: required"),
    )
    class Meta:
       verbose_name = _("Club Championship Score")
       verbose_name_plural = _("Club Championship Scores")
    def __str__(self):
       return f"{self.clubchampionship} - {self.archer} - {self.score}"
    def __unicode__(self):
       return f"{self.clubchampionship} - {self.archer} - {self.score}"

class PersonalBest(BaseModel):
    """
    Model representing a personal best score for an archer in a specific competition.
    """

    # id is a UUID field that serves as the primary key for the PersonalBest model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # archer is a foreign key to the Archer model, indicating which archer achieved the personal best.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("personalbest archer"),
        help_text=_("format: required"),
        related_name='personalbests'
    )
    # competition is a foreign key to the Competition model, indicating in which competition the personal best was achieved.
    competition = models.ForeignKey(
        Competition,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("personalbest competition"),
        help_text=_("format: required"),
        related_name='personalbest_competition'
    )
    # score is a positive integer field indicating the personal best score achieved by the archer.
    score = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("personalbest points"),
        help_text=_("format: required"),
    )

    class Meta:
       verbose_name = _("Personal Best")
       verbose_name_plural = _("Personal Bests")

    def __str__(self):
       return f"{self.archer} - {self.competition} - {self.score}"
    def __unicode__(self):
       return f"{self.archer} - {self.competition} - {self.score}"

class PersonalBestMembership(BaseModel):
    """
    Model representing the relationship between a personal best and an archer.
    """

    # id is a UUID field that serves as the primary key for the PersonalBestMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # personalbest is a foreign key to the PersonalBest model, indicating which personal best is being associated with the archer.
    personalbest = models.ForeignKey(
        PersonalBest,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("personalbestmembership personalbest"),
        help_text=_("format: required"),
        related_name='personalbestmemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer achieved the personal best.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("personalbestmembership archer"),
        help_text=_("format: required"),
        related_name='personalbestmembership_archer'
    )

class BestOfClub(BaseModel):
    """
    Model representing the best score of an archer in a club.
    """

    # id is a UUID field that serves as the primary key for the BestOfClub model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # archer is a foreign key to the Archer model, indicating which archer achieved the best score.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bestofclub archer"),
        help_text=_("format: required"),
        related_name='bestofclubs'
    )
    # score is a positive integer field indicating the best score achieved by the archer in the club.
    score = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("bestofclub points"),
        help_text=_("format: required"),
    )

    class Meta:
       verbose_name = _("Best of Club")
       verbose_name_plural = _("Best of Clubs")
    def __str__(self):
       return f"{self.archer} - {self.score}"
    def __unicode__(self):
       return f"{self.archer} - {self.score}"
class BestOfClubMembership(BaseModel):
    """
    Model representing the relationship between a best of club and an archer.
    """

    # id is a UUID field that serves as the primary key for the BestOfClubMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bestofclub is a foreign key to the BestOfClub model, indicating which best of club is being associated with the archer.
    bestofclub = models.ForeignKey(
        BestOfClub,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bestofclubmembership bestofclub"),
        help_text=_("format: required"),
        related_name='bestofclubmemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer achieved the best score.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bestofclubmembership archer"),
        help_text=_("format: required"),
        related_name='bestofclubmembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the best of club membership.
    # It uses PROTECT to prevent deletion of the user if there are best of club memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the best of club memberships created by a user.
    # This is useful for querying all best of club memberships associated with a specific user.
    # The author field is not unique, allowing multiple best of club memberships to be created by the same user.
    # This is useful for cases where multiple best of club memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of best of club membership"),
        related_name='bestofclubmembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    class Meta:
        # verbose_name is the singular name for the BestOfClubMembership model.
        verbose_name = _("Best of Club Membership")
        # verbose_name_plural is the plural name for the BestOfClubMembership model.
        verbose_name_plural = _("Best of Club Memberships")
    def __str__(self):
        """
        Returns a string representation of the BestOfClubMembership instance.
        This representation includes the archer and best of club details.
        """
        return f"{str(self.archer)} - {str(self.bestofclub)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the BestOfClubMembership instance.
        This representation includes the archer and best of club details.
        """
        return f"{str(self.archer)} - {str(self.bestofclub)}"

class Accessory(BaseModel):
    """
    Model representing an accessory used in archery.
    """

    # id is a UUID field that serves as the primary key for the Accessory model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the accessory, which describes the accessory type.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("accessory name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the accessory.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple accessories to have the same slug.
    # This is useful for cases where multiple accessories may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the accessory's name.
    # This allows for easy identification of the accessory in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a text field for additional information about the accessory.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple accessories to have the same information.
    # This is useful for cases where accessories may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that accessories may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("accessory information"),
        help_text=_("format: not required"),
    )

    # author is a foreign key to the User model, indicating who created the accessory.
    # It uses PROTECT to prevent deletion of the user if there are accessories linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the accessories created by a user.
    # This is useful for querying all accessories associated with a specific user.
    # The author field is not unique, allowing multiple accessories to be created by the same user.
    # This is useful for cases where multiple accessories are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of accessory"),
        related_name='accessory_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
       verbose_name = _("Accessory")
       verbose_name_plural = _("Accessories")

    def __str__(self):
       return self.name

    def __unicode__(self):
       return self.name

class ArcherAccessory(BaseModel):
    """
    Model representing the relationship between an archer and an accessory.
    This model is used to track which accessories are used by which archers.
    """

    # id is a UUID field that serves as the primary key for the ArcherAccessory model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # accessory is a foreign key to the Accessory model, indicating which accessory is being used by the archer.
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archeraccessory accessory"),
        help_text=_("format: required"),
        related_name='archeraccessories'
    )
    # archer is a foreign key to the Archer model, indicating which archer is using the accessory.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archeraccessory archer"),
        help_text=_("format: required"),
        related_name='archeraccessory_archer'
    )

    # author is a foreign key to the User model, indicating who created the archer accessory relationship.
    # It uses PROTECT to prevent deletion of the user if there are archer accessories linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the archer accessories created by a user.
    # This is useful for querying all archer accessories associated with a specific user.
    # The author field is not unique, allowing multiple archer accessories to be created by the same user.
    # This is useful for cases where multiple archer accessories are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of archer accessory"),
        related_name='archeraccessory_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the ArcherAccessory model.
        verbose_name = _("Archer Accessory")
        # verbose_name_plural is the plural name for the ArcherAccessory model.
        verbose_name_plural = _("Archer Accessories")

    def __str__(self):
        """
        Returns a string representation of the ArcherAccessory instance.
        This representation includes the archer and accessory names.
        """
        return f"{str(self.archer)} - {str(self.accessory)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the ArcherAccessory instance.
        This representation includes the archer and accessory names.
        """
        return f"{str(self.archer)} - {str(self.accessory)}"

class ArcherAccessoryMembership(BaseModel):
    """
    Model representing the relationship between an archer accessory and an archer.
    This model is used to track which archers are associated with which accessories.
    """

    # id is a UUID field that serves as the primary key for the ArcherAccessoryMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # archeraccessory is a foreign key to the ArcherAccessory model, indicating which accessory is being associated with the archer.
    archeraccessory = models.ForeignKey(
        ArcherAccessory,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archeraccessorymembership archeraccessory"),
        help_text=_("format: required"),
        related_name='archeraccessorymemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is being associated with the accessory.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archeraccessorymembership archer"),
        help_text=_("format: required"),
        related_name='archeraccessorymembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the archer accessory membership.
    # It uses PROTECT to prevent deletion of the user if there are archer accessory memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the archer accessory memberships created by a user.
    # This is useful for querying all archer accessory memberships associated with a specific user.
    # The author field is not unique, allowing multiple archer accessory memberships to be created by the same user.
    # This is useful for cases where multiple archer accessory memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of archer accessory membership"),
        related_name='archeraccessorymembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the ArcherAccessoryMembership model.
        verbose_name = _("Archer Accessory Membership")
        # verbose_name_plural is the plural name for the ArcherAccessoryMembership model.
        verbose_name_plural = _("Archer Accessory Memberships")

    def __str__(self):
        """
        Returns a string representation of the ArcherAccessoryMembership instance.
        This representation includes the archer and accessory names.
        """
        return f"{str(self.archer)} - {str(self.archeraccessory)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the ArcherAccessoryMembership instance.
        This representation includes the archer and accessory names.
        """
        return f"{str(self.archer)} - {str(self.archeraccessory)}"
class BowSightAccessory(BaseModel):
    """
    Model representing the relationship between a bow sight and an accessory.
    This model is used to track which accessories are associated with which bow sights.
    """
    # id is a UUID field that serves as the primary key for the BowSightAccessory model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bowsight is a foreign key to the BowSight model, indicating which bow sight is being associated with the accessory.
    bowsight = models.ForeignKey(
        BowSight,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsightaccessory bowsight"),
        help_text=_("format: required"),
        related_name='bowsightaccessories'
    )
    # accessory is a foreign key to the Accessory model, indicating which accessory is being associated with the bow sight.
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsightaccessory accessory"),
        help_text=_("format: required"),
        related_name='bowsightaccessory_accessory'
    )

    # author is a foreign key to the User model, indicating who created the bow sight accessory relationship.
    # It uses PROTECT to prevent deletion of the user if there are bow sight accessories linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow sight accessories created by a user.
    # This is useful for querying all bow sight accessories associated with a specific user.
    # The author field is not unique, allowing multiple bow sight accessories to be created by the same user.
    # This is useful for cases where multiple bow sight accessories are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow sight accessory"),
        related_name='bowsightaccessory_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the BowSightAccessory model.
        verbose_name = _("Bow Sight Accessory")
        # verbose_name_plural is the plural name for the BowSightAccessory model.
        verbose_name_plural = _("Bow Sight Accessories")

    def __str__(self):
        """
        Returns a string representation of the BowSightAccessory instance.
        This representation includes the bow sight and accessory names.
        """
        return f"{str(self.bowsight)} - {str(self.accessory)}"
    def __unicode__(self):
        """
        Returns a unicode representation of the BowSightAccessory instance.
        This representation includes the bow sight and accessory names.
        """
        return f"{str(self.bowsight)} - {str(self.accessory)}"
class BowSightAccessoryMembership(BaseModel):
    """
    Model representing the relationship between a bow sight accessory and an archer.
    This
    model is used to track which archers are associated with which bow sight accessories.
    """
    # id is a UUID field that serves as the primary key for the BowSightAccessoryMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bowsightaccessory is a foreign key to the BowSightAccessory model, indicating which bow sight accessory is being associated with the archer.
    bowsightaccessory = models.ForeignKey(
        BowSightAccessory,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsightaccessorymembership bowsightaccessory"),
        help_text=_("format: required"),
        related_name='bowsightaccessorymemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is being associated with the bow sight accessory.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowsightaccessorymembership archer"),
        help_text=_("format: required"),
        related_name='bowsightaccessorymembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the bow sight accessory membership.
    # It uses PROTECT to prevent deletion of the user if there are bow sight accessory memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow sight accessory memberships created by a user.
    # This is useful for querying all bow sight accessory memberships associated with a specific user.
    # The author field is not unique, allowing multiple bow sight accessory memberships to be created by the same user.
    # This is useful for cases where multiple bow sight accessory memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow sight accessory membership"),
        related_name='bowsightaccessorymembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the BowSightAccessoryMembership model.
        verbose_name = _("Bow Sight Accessory Membership")
        # verbose_name_plural is the plural name for the BowSightAccessoryMembership model.
        verbose_name_plural = _("Bow Sight Accessory Memberships")

    def __str__(self):
        """
        Returns a string representation of the BowSightAccessoryMembership instance.
        This representation includes the archer and bow sight accessory names.
        """
        return f"{str(self.archer)} - {str(self.bowsightaccessory)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the BowSightAccessoryMembership instance.
        This representation includes the archer and bow sight accessory names.
        """
        return f"{str(self.archer)} - {str(self.bowsightaccessory)}"

class Bow(BaseModel):
    """
    Model representing a bow used in archery.
    """

    # id is a UUID field that serves as the primary key for the Bow model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # name is a required field for the bow, which describes the bow type.
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("bow name"),
        help_text=_("format: required, max-64")
    )

    # slug is an AutoSlugField that automatically generates a slug from the name of the bow.
    # It is editable and can be used for URL-friendly representations.
    # The slug field is not unique, allowing multiple bows to have the same slug.
    # This is useful for cases where multiple bows may share similar names or are located in different areas.
    # The slug is generated from the name field, ensuring that it is always based on the bow's name.
    # This allows for easy identification of the bow in URLs and other contexts.
    # The slug field is editable, allowing users to change it if needed.
    slug = AutoSlugField(populate_from='name',editable=True)

    # info is a text field for additional information about the bow.
    # It is not required and can be blank.
    # The info field is not unique, allowing multiple bows to have the same information.
    # This is useful for cases where bows may want to provide additional details or descriptions.
    # It is a TextField, which means it can store large amounts of text.
    # It is allowed to be null or blank, meaning that bows may not have additional information.
    # The info field is editable, allowing users to change it if needed.
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bow information"),
        help_text=_("format: not required"),
    )
    # author is a foreign key to the User model, indicating who created the bow.
    # It uses PROTECT to prevent deletion of the user if there are bows linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bows created by a user.
    # This is useful for querying all bows associated with a specific user.
    # The author field is not unique, allowing multiple bows to be created by the same user.
    # This is useful for cases where multiple bows are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow"),
        related_name='bow_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
       verbose_name = _("Bow")
       verbose_name_plural = _("Bows")
    def __str__(self):
       return self.name
    def __unicode__(self):
       return self.name
class BowMembership(BaseModel):
    """
    Model representing the relationship between a bow and an archer.
    This
    model is used to track which bows are used by which archers.
    """
    # id is a UUID field that serves as the primary key for the BowMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bow is a foreign key to the Bow model, indicating which bow is being used by the archer.
    bow = models.ForeignKey(
        Bow,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowmembership bow"),
        help_text=_("format: required"),
        related_name='bowmemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is using the bow.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowmembership archer"),
        help_text=_("format: required"),
        related_name='bowmembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the bow membership.
    # It uses PROTECT to prevent deletion of the user if there are bow memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow memberships created by a user.
    # This is useful for querying all bow memberships associated with a specific user.
    # The author field is not unique, allowing multiple bow memberships to be created by the same user.
    # This is useful for cases where multiple bow memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow membership"),
        related_name='bowmembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields

    class Meta:
        # verbose_name is the singular name for the BowMembership model.
        verbose_name = _("Bow Membership")
        # verbose_name_plural is the plural name for the BowMembership model.
        verbose_name_plural = _("Bow Memberships")

    def __str__(self):
        """
        Returns a string representation of the BowMembership instance.
        This representation includes the archer and bow names.
        """
        return f"{str(self.archer)} - {str(self.bow)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the BowMembership instance.
        This representation includes the archer and bow names.
        """
        return f"{str(self.archer)} - {str(self.bow)}"

class BowAccessory(BaseModel):
    """
    Model representing the relationship between a bow and an accessory.
    This model is used to track which accessories are associated with which bows.
    """

    # id is a UUID field that serves as the primary key for the BowAccessory model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bow is a foreign key to the Bow model, indicating which bow is being associated with the accessory.
    bow = models.ForeignKey(
        Bow,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowaccessory bow"),
        help_text=_("format: required"),
        related_name='bowaccessories'
    )
    # accessory is a foreign key to the Accessory model, indicating which accessory is being associated with the bow.
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowaccessory accessory"),
        help_text=_("format: required"),
        related_name='bowaccessory_accessory'
    )

    # author is a foreign key to the User model, indicating who created the bow accessory relationship.
    # It uses PROTECT to prevent deletion of the user if there are bow accessories linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow accessories created by a user.
    # This is useful for querying all bow accessories associated with a specific user.
    # The author field is not unique, allowing multiple bow accessories to be created by the same user.
    # This is useful for cases where multiple bow accessories are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow accessory"),
        related_name='bowaccessory_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the BowAccessory model.
        verbose_name = _("Bow Accessory")
        # verbose_name_plural is the plural name for the BowAccessory model.
        verbose_name_plural = _("Bow Accessories")

    def __str__(self):
        """
        Returns a string representation of the BowAccessory instance.
        This representation includes the bow and accessory names.
        """
        return f"{str(self.bow)} - {str(self.accessory)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the BowAccessory instance.
        This representation includes the bow and accessory names.
        """
        return f"{str(self.bow)} - {str(self.accessory)}"

class BowAccessoryMembership(BaseModel):
    """
    Model representing the relationship between a bow accessory and an archer.
    This model is used to track which archers are associated with which bow accessories.
    """

    # id is a UUID field that serves as the primary key for the BowAccessoryMembership model.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # bowaccessory is a foreign key to the BowAccessory model, indicating which bow accessory is being associated with the archer.
    bowaccessory = models.ForeignKey(
        BowAccessory,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowaccessorymembership bowaccessory"),
        help_text=_("format: required"),
        related_name='bowaccessorymemberships'
    )
    # archer is a foreign key to the Archer model, indicating which archer is being associated with the bow accessory.
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowaccessorymembership archer"),
        help_text=_("format: required"),
        related_name='bowaccessorymembership_archer'
    )

    # author is a foreign key to the User model, indicating who created the bow accessory membership.
    # It uses PROTECT to prevent deletion of the user if there are bow accessory memberships linked to them.
    # The default value is set to 1, which should be the ID of a superuser or a default user.
    # related_name allows reverse access to the bow accessory memberships created by a user.
    # This is useful for querying all bow accessory memberships associated with a specific user.
    # The author field is not unique, allowing multiple bow accessory memberships to be created by the same user.
    # This is useful for cases where multiple bow accessory memberships are managed by the same user.
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of bow accessory membership"),
        related_name='bowaccessorymembership_author',
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        # verbose_name is the singular name for the BowAccessoryMembership model.
        verbose_name = _("Bow Accessory Membership")
        # verbose_name_plural is the plural name for the BowAccessoryMembership model.
        verbose_name_plural = _("Bow Accessory Memberships")

    def __str__(self):
        """
        Returns a string representation of the BowAccessoryMembership instance.
        This representation includes the archer and bow accessory names.
        """
        return f"{str(self.archer)} - {str(self.bowaccessory)}"

    def __unicode__(self):
        """
        Returns a unicode representation of the BowAccessoryMembership instance.
        This representation includes the archer and bow accessory names.
        """
        return f"{str(self.archer)} - {str(self.bowaccessory)}"

