from django.contrib import admin
from api.models import (
    Archer,
    Club,
    Membership,
    Category,
    CategoryMembership,
    BowType,
    BowTypeMembership,
    Team,
    TeamMembership,
    Contest,
    ContestMembership,
    User,
    TargetFace,
    ScoringSheet,
    Result,
    Competition,
    CompetitionMembership,
)

class ArcherAdmin(admin.ModelAdmin):
    """
    Admin interface for managing archers.
    This class defines how archers are displayed and managed in the Django admin interface.
    It includes fields for personal information, contact details, and extra information such as birth date.
    """
    list_display = ('last_name', 'first_name', 'middle_name')
    list_display_links = ('last_name', 'first_name')
    list_per_page = 20
    ordering = ('last_name', 'first_name')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'middle_name', 'last_name', )
        }),
        ('Contact Information', {
            'classes': ['collapse'],
            'fields': ('email', 'phone', 'address', 'city', 'zip_code',),
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('birth_date',),
        }),
    )
    search_fields = ('last_name', 'first_name', 'middle_name')
    
class MembershipInline(admin.TabularInline):
    """
    Inline admin interface for managing memberships of archers in clubs.
    This class allows quick access to the membership details of an archer within the club admin interface.
    It displays the archer's name, start date, and end date of the membership.
    """
    model = Membership
    extra = 1
    fields = ('archer', 'start_date', 'end_date')
    readonly_fields = ('archer', 'start_date', 'end_date')
    can_delete = False
    show_change_link = True

class ClubAdmin(admin.ModelAdmin):
    """
    Admin interface for managing clubs.
    This class defines how clubs are displayed and managed in the Django admin interface.
    It includes inline management for memberships, allowing quick access to club members.
    """
    inlines = [
        MembershipInline
    ]
    list_display = ('name', 'town')
    list_display_links = ('name', 'town')
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'town')
        }),
    )

class MembershipAdmin(admin.ModelAdmin):
    """
    Admin interface for managing memberships of archers in clubs.
    This class defines how memberships are displayed and managed in the Django admin interface.
    It includes fields for the archer, club, start date, and end date of the membership.
    """
    list_display = ('archer', 'club', 'start_date', 'end_date')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'club')
    fieldsets = (
        (None, {
            'fields': ('archer', 'club', 'start_date', 'end_date')
        }),
    )
    search_fields = ('archer__last_name', 'club__name')

class CategoryMembershipInline(admin.TabularInline):
    """
    Inline admin interface for managing category memberships of archers.
    This class allows quick access to the category details of an archer within the category admin interface.
    It displays the archer's name and the category they belong to.
    """
    model = CategoryMembership
    extra = 1
    fields = ('archer', 'category')
    can_delete = False
    show_change_link = True

class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing categories.
    This class defines how categories are displayed and managed in the Django admin interface.
    It includes inline management for category memberships, allowing quick access to the archers in each category.
    """
    inlines = [
        CategoryMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
    search_fields = ('name',)

class CategoryMembershipAdmin(admin.ModelAdmin):
    """
    Admin interface for managing category memberships of archers.
    This class defines how category memberships are displayed and managed in the Django admin interface.
    It includes fields for the archer and the category they belong to.
    """
    list_display = ('archer', 'category')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'category')
    fieldsets = (
        (None, {
            'fields': ('archer', 'category')
        }),
    )
    search_fields = ('archer__last_name', 'category__name')
    
class BowtypeMembershipInline(admin.TabularInline):
    """
    Inline admin interface for managing bow type memberships of archers.
    This class allows quick access to the bow type details of an archer within the bow type admin interface.
    It displays the archer's name and the bow type they belong to.
    """
    model = BowTypeMembership
    extra = 1
    fields = ('archer', 'bowtype')
    can_delete = False
    show_change_link = True

class BowtypeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing bow types.
    This class defines how bow types are displayed and managed in the Django admin interface.
    It includes inline management for bow type memberships, allowing quick access to the archers using each bow type.
    """
    inlines = [
        BowtypeMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info')
        }),
    )
    search_fields = ('name',)

class BowTypeMembershipAdmin(admin.ModelAdmin):
    """
    Admin interface for managing bow type memberships of archers.
    This class defines how bow type memberships are displayed and managed in the Django admin interface.
    It includes fields for the archer and the bow type they belong to.
    """
    list_display = ('archer', 'bowtype')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'bowtype')
    fieldsets = (
        (None, {
            'fields': ('archer', 'bowtype'),
        }),
    )
    search_fields = ('archer__last_name', 'bowtype__name')

class TeamMembershipInline(admin.TabularInline):
    """
    Inline admin interface for managing team memberships of archers.
    This class allows quick access to the team details of an archer within the team admin interface.
    It displays the archer's name and the team they belong to.
    """
    model = TeamMembership
    extra = 1
    fields = ('archer', 'team')
    can_delete = False
    show_change_link = True

class TeamAdmin(admin.ModelAdmin):
    """
    Admin interface for managing teams.
    This class defines how teams are displayed and managed in the Django admin interface.
    It includes inline management for team memberships, allowing quick access to the archers in each team.
    """
    inlines = [
        TeamMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
    search_fields = ('name',)
    
class TeamMembershipAdmin(admin.ModelAdmin):
    """
    Admin interface for managing team memberships of archers.
    This class defines how team memberships are displayed and managed in the Django admin interface.
    It includes fields for the archer and the team they belong to.
    """
    list_display = ('archer', 'team')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'team')
    fieldsets = (
        (None, {
            'fields': ('archer', 'team')
        }),
    )
    search_fields = ('archer__last_name', 'team__name')
    
class ContestMembershipInline(admin.TabularInline):
    """
    Inline admin interface for managing contest memberships of archers.
    This class allows quick access to the contest details of an archer within the contest admin interface.
    It displays the archer's name and the contest they are participating in.
    """
    model = ContestMembership
    extra = 1
    fields = ('archer', 'contest')
    can_delete = False
    show_change_link = True

class ContestAdmin(admin.ModelAdmin):
    """
    Admin interface for managing contests.
    This class defines how contests are displayed and managed in the Django admin interface.
    It includes inline management for contest memberships, allowing quick access to the archers participating in each contest.
    """
    inlines = [
        ContestMembershipInline
    ]
    list_display = ('name', 'start_date', 'start_time')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'start_date', 'start_time', 'info')
        }),
    )
    search_fields = ('name',)

class ContestMembershipAdmin(admin.ModelAdmin):
    """
    Admin interface for managing contest memberships of archers.
    This class defines how contest memberships are displayed and managed in the Django admin interface.
    It includes fields for the archer and the contest they are participating in.
    """
    list_display = ('archer', 'contest')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'contest')
    fieldsets = (
        (None, {
            'fields': ('archer', 'contest')
        }),
    )
    search_fields = ('archer__last_name', 'contest__name')

class TargetFaceAdmin(admin.ModelAdmin):
    """
    Admin interface for managing target faces.
    This class defines how target faces are displayed and managed in the Django admin interface.
    It includes fields for the name, diameter, and additional information about the target face.
    """
    list_display = ('name', 'diameter')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'diameter', 'info') 
        }),
    )
    search_fields = ('name',)

class ScoringSheetAdmin(admin.ModelAdmin):
    """
    Admin interface for managing scoring sheets.
    This class defines how scoring sheets are displayed and managed in the Django admin interface.
    It includes fields for the name of the scoring sheet and additional information.
    """

    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info')
        }),
    )
    search_fields = ('name',)

class ResultAdmin(admin.ModelAdmin):
    """
    Admin interface for managing results of contests.
    This class defines how results are displayed and managed in the Django admin interface.
    It includes fields for the contest, archer, score, and additional information.
    """

    list_display = ('contest', 'archer', 'score')
    list_display_links = ('contest',)
    list_per_page = 20
    ordering = ('contest', 'archer')
    fieldsets = (
        (None, {
            'fields': ('contest', 'archer', 'score','info')
        }),
    )
    search_fields = ('contest__name', 'archer__last_name')
        
class CompetitionMembershipInline(admin.TabularInline):
    """
    Inline admin interface for managing competition memberships of archers.
    This class allows quick access to the competition details of an archer within the competition admin interface.
    It displays the archer's name and the competition they are participating in.
    """

    model = CompetitionMembership
    extra = 1
    fields = ('archer', 'competition')
    can_delete = False
    show_change_link = True

class CompetitionAdmin(admin.ModelAdmin):
    """
    Admin interface for managing competitions.
    This class defines how competitions are displayed and managed in the Django admin interface.
    It includes inline management for competition memberships, allowing quick access to the archers participating in each competition.
    """
    
    inlines = [
        CompetitionMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info')
        }),
    )
    search_fields = ('name',)

class CompetitionMembershipAdmin(admin.ModelAdmin):
    """
    Admin interface for managing competition memberships of archers.
    This class defines how competition memberships are displayed and managed in the Django admin interface.
    It includes fields for the archer and the competition they are participating in.
    """

    list_display = ('archer', 'competition')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'competition')
    fieldsets = (
        (None, {
            'fields': ('archer', 'competition')
        }),
    )
    search_fields = ('archer__last_name', 'competition__name')
        
class UserAdmin(admin.ModelAdmin):
    """
    Admin interface for managing users.
    This class defines how users are displayed and managed in the Django admin interface.
    It includes fields for the username, email, first name, last name, and status (staff and active).
    """

    list_display = ('username', 'email')
    list_display_links = ('username',)
    list_per_page = 20
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
        }),
    )

admin.site.register(Archer, ArcherAdmin)

admin.site.register(Club, ClubAdmin)
admin.site.register(Membership, MembershipAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryMembership, CategoryMembershipAdmin)

admin.site.register(BowType, BowtypeAdmin)
admin.site.register(BowTypeMembership, BowTypeMembershipAdmin)

admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMembership, TeamMembershipAdmin)

admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestMembership, ContestMembershipAdmin)

admin.site.register(TargetFace, TargetFaceAdmin)

admin.site.register(ScoringSheet, ScoringSheetAdmin)

admin.site.register(Result, ResultAdmin)

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(CompetitionMembership, CompetitionMembershipAdmin)

admin.site.register(User, UserAdmin)

        # ('Specific fields', {
        #     'classes': ['collapse'],
        #     'fields': (
        #         'type_of_bow',
                
        #         'bow_length',
        #         'bow_weight',
        #         'bow_weight_units',
        #         'bow_material',
        #         'bow_color',
        #         'bow_string_type',
        #         'bow_string_length',
        #         'bow_string_weight',
        #         'bow_string_weight_units',
        #         'bow_string_material',
        #         'bow_string_color',

        #         'bow_riser_type',
        #         'bow_riser_length',
        #         'bow_riser_weight',
        #         'bow_riser_weight_units',
        #         'bow_riser_material',
        #         'bow_riser_color',

        #         'bow_limbs_type',
        #         'bow_limbs_length',
        #         'bow_limbs_weight',
        #         'bow_limbs_weight_units',
        #         'bow_limbs_material',
        #         'bow_limbs_color',
        #         'bow_limbs_tension',
        #         'bow_limbs_tension_units',
        #         'bow_limbs_tension_max',
        #         'bow_limbs_tension_min',
        #         'bow_limbs_tension_max_units',
        #         'bow_limbs_tension_min_units',
                
        #         'bow_handle_type',
        #         'bow_handle_length',
        #         'bow_handle_weight',
        #         'bow_handle_weight_units',
        #         'bow_handle_material',
        #         'bow_handle_color',
        #         'bow_handle_tension',
        #         'bow_handle_tension_units',
        #         'bow_handle_tension_max',
        #         'bow_handle_tension_min',
        #         'bow_handle_tension_max_units',
        #         'bow_handle_tension_min_units',
            
        #         'type_of_string',
        #         'string_length',
        #         'string_weight',
        #         'string_weight_units',
        #         'string_material',
        #         'string_color',
        #         'string_tension',
        #         'string_tension_units',
        #         'string_tension_max',
        #         'string_tension_min',
        #         'string_tension_max_units',
        #         'string_tension_min_units',
                

        #         'max_draw_length',
        #         'min_draw_length',
        #         'max_draw_weight',
        #         'min_draw_weight',
        #         'draw_weight_units',
                
        #         'max_arrow_length',
        #         'min_arrow_length',
        #         'max_arrow_weight',
        #         'min_arrow_weight',
        #         'max_arrow_diameter',
        #         'min_arrow_diameter',
        #         'max_arrow_spine',
        #         'min_arrow_spine',
        #         'max_arrow_fletchings',
        #         'min_arrow_fletchings',
        #         'max_arrow_fletchings_length',
        #         'min_arrow_fletchings_length',
        #         'max_arrow_nock_type',
        #         'min_arrow_nock_type',
        #         'max_arrow_point_type',                
        #         'min_arrow_point_type',
        #         'max_arrow_point_weight',
        #         'min_arrow_point_weight',
        #         'max_arrow_point_diameter',
        #         'min_arrow_point_diameter',
        #         'max_arrow_point_length',
        #         'min_arrow_point_length',
        #         'max_arrow_fletchings_angle',                
        #         'min_arrow_fletchings_angle',
        #         'max_arrow_fletchings_material',
        #         'min_arrow_fletchings_material',
        #         'max_arrow_fletchings_color',
        #         'min_arrow_fletchings_color',
        #         'max_arrow_fletchings_shape',
        #         'min_arrow_fletchings_shape',
        #         'max_arrow_fletchings_spacing',
        #         'min_arrow_fletchings_spacing',
        #         'max_arrow_fletchings_orientation',
        #         'min_arrow_fletchings_orientation',
        #         'max_arrow_fletchings_quantity',
        #         'min_arrow_fletchings_quantity',
        #         'max_arrow_fletchings_weight',
        #         'min_arrow_fletchings_weight',
        #         'min_arrow_fletchings_length',
        #         'max_arrow_fletchings_width',
        #         'min_arrow_fletchings_width',
        #         'max_arrow_fletchings_height',
        #         'min_arrow_fletchings_height',
        #         'max_arrow_fletchings_thickness',
        #         'min_arrow_fletchings_thickness',
        #         'max_arrow_fletchings_taper',
        #         'min_arrow_fletchings_taper',
        #         'max_arrow_fletchings_taper_angle',
        #         'min_arrow_fletchings_taper_angle',
        #         'max_arrow_fletchings_taper_length',
        #         'min_arrow_fletchings_taper_length',
        #         'max_arrow_fletchings_taper_width',
        #         'min_arrow_fletchings_taper_width',
        #         'max_arrow_fletchings_taper_height',
        #         'min_arrow_fletchings_taper_height',
        #         'max_arrow_fletchings_taper_thickness',
        #         'min_arrow_fletchings_taper_thickness',
        #         'max_arrow_fletchings_taper_shape',
        #         'min_arrow_fletchings_taper_shape',
        #         'max_arrow_fletchings_taper_material',
        #         'min_arrow_fletchings_taper_material',
        #         'max_arrow_fletchings_taper_color',
        #         'min_arrow_fletchings_taper_color',
        #         'max_arrow_fletchings_taper_quantity',
        #         'min_arrow_fletchings_taper_quantity',
        #         'max_arrow_fletchings_taper_weight',
        #         'min_arrow_fletchings_taper_weight',

        #         'fletching_type',
        #         'fletching_length',
        #         'fletching_width',
        #         'fletching_height',
        #         'fletching_thickness',
        #         'fletching_taper',
        #         'fletching_taper_angle',
        #         'fletching_taper_length',
        #         'fletching_taper_width',
        #         'fletching_taper_height',
        #         'fletching_taper_thickness',
        #         'fletching_taper_shape',
        #         'fletching_taper_material',
        #         'fletching_taper_color',
        #         'fletching_taper_quantity',
        #         'fletching_taper_weight',
        #         'fletching_taper_diameter',
        #         'arrow_length',
        #         'arrow_weight',
        #         'arrow_diameter',
        #         'arrow_spine',
        #         'arrow_fletchings',
        #         'arrow_nock_type',
                
        #     ),
        # }),
