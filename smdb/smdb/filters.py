from django import forms
from django_filters import (
    FilterSet,
    CharFilter,
    ChoiceFilter,
    ModelMultipleChoiceFilter,
)
from django.db.utils import ProgrammingError
from smdb.models import Mission, Expedition, Compilation, Quality_Category

from django.forms.widgets import TextInput


class MissionFilter(FilterSet):
    name = CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="",
        widget=TextInput(attrs={"placeholder": "Name contains..."}),
    )
    try:
        region_name = ChoiceFilter(
            field_name="region_name",
            choices=[
                (m, m)
                for m in Mission.objects.values_list("region_name", flat=True).distinct()
            ],
            label="",
            empty_label="- region -",
            widget=forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "font-weight: 300; font-size: smaller;",
                }
            ),
        )
    except ProgrammingError as e:
        # Likely error on initial migrate done with start command creating the smdb database
        pass
    quality_categories = ModelMultipleChoiceFilter(
        field_name="quality_categories__name",
        queryset=Quality_Category.objects.all(),
        to_field_name="name",
        label="",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control", "size": 2, "style": "font-size: x-small;"}
        ),
    )
    patch_test = ChoiceFilter(
        field_name="patch_test",
        choices=[(None, "-"), (True, "✔")],
        label="",
        empty_label="- Patch Test -",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "style": "font-weight: 300; font-size: smaller;",
            }
        ),
    )
    repeat_survey = ChoiceFilter(
        field_name="repeat_survey",
        choices=[(None, "-"), (True, "✔")],
        label="",
        empty_label="- Repeat Survey -",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "style": "font-weight: 300; font-size: smaller;",
            }
        ),
    )
    try:
        mgds_compilation = ChoiceFilter(
            field_name="mgds_compilation",
            choices=[
                (m, m)
                for m in Mission.objects.values_list(
                    "mgds_compilation", flat=True
                ).distinct()
            ],
            label="",
            empty_label="- MGDS_compilation -",
            widget=forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "font-weight: 300; font-size: smaller;",
                }
            ),
        )
    except ProgrammingError as e:
        # Likely error on initial migrate done with start command creating the smdb database
        pass
    expedition__name = CharFilter(
        field_name="expedition__name",
        lookup_expr="icontains",
        label="",
        widget=TextInput(attrs={"placeholder": "Expedition name contains..."}),
    )

    class Meta:
        model = Mission
        fields = [
            "name",
            "region_name",
            "quality_categories",
            "patch_test",
            "repeat_survey",
            "mgds_compilation",
            "expedition__name",
        ]


class ExpeditionFilter(FilterSet):
    name = CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="",
        widget=TextInput(attrs={"placeholder": "Name contains..."}),
    )

    class Meta:
        model = Expedition
        fields = [
            "name",
        ]


class CompilationFilter(FilterSet):
    name = CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="",
        widget=TextInput(attrs={"placeholder": "Name contains..."}),
    )

    class Meta:
        model = Compilation
        fields = [
            "name",
        ]
