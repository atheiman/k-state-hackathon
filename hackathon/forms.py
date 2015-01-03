from django import forms

from .models import Team, Judge, Review, Entrant, User
from .global_vars import YEAR_IN_SCHOOL_CHOICES, MAJOR_CHOICES



project_name_char_field = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            'placeholder':'Our Awesome Project',
        })
        help_text="Good project names are short and memorable. This can be changed later.",
    )



class CreateTeamForm(forms.Form):
    """Create a team and the Users and Entrants that are members of the team."""
    project_name = project_name_char_field

    leader_eid = forms.CharField(
        max_length=40,
    )
    leader_year_in_school = forms.ChoiceField(
        choices=YEAR_IN_SCHOOL_CHOICES,
    )
    leader_major = forms.ChoiceField(
        choices=MAJOR_CHOICES,
    )

    member_2_eid = forms.CharField(
        max_length=40,
    )
    member_2_year_in_school = forms.ChoiceField(
        choices=YEAR_IN_SCHOOL_CHOICES,
    )
    member_2_major = forms.ChoiceField(
        choices=MAJOR_CHOICES,
    )

    member_3_eid = forms.CharField(
        max_length=40,
        required=False,
    )
    member_3_year_in_school = forms.ChoiceField(
        choices=YEAR_IN_SCHOOL_CHOICES,
        required=False,
    )
    member_3_major = forms.ChoiceField(
        choices=MAJOR_CHOICES,
        required=False,
    )

    member_4_eid = forms.CharField(
        max_length=40,
        required=False,
    )
    member_4_year_in_school = forms.ChoiceField(
        choices=YEAR_IN_SCHOOL_CHOICES,
        required=False,
    )
    member_4_major = forms.ChoiceField(
        choices=MAJOR_CHOICES,
        required=False,
    )

    member_5_eid = forms.CharField(
        max_length=40,
        required=False,
    )
    member_5_year_in_school = forms.ChoiceField(
        choices=YEAR_IN_SCHOOL_CHOICES,
        required=False,
    )
    member_5_major = forms.ChoiceField(
        choices=MAJOR_CHOICES,
        required=False,
    )



class EditTeamForm(forms.Form):
    """Edit the team info."""
    project_name = project_name_char_field
    project_description = forms.CharField(
        required=False,
        help_text="Explain your team's project. What need does this fill? How do you use it? What open-source technologies have you leveraged? What did you learn while working on this project? This description is a component of your team's score.",
        widget=forms.Textarea(attrs={
            'placeholder':'What makes our project awesome is...',
        })
    )
    project_repository = forms.URLField(
        required=False,
        help_text="URL of your project code repository. We recommend using <a href='https://github.com/' target='blank'>GitHub</a> for repository hosting.",
        widget=forms.TextInput(attrs={
            'placeholder':'https://github.com/johndoe/some-awesome-project',
        })
    )



class ReviewForm(forms.ModelForm):
    """Submit a review for a team."""
    class Meta:
        model = Review
        exclude = ['created', 'judge',]
