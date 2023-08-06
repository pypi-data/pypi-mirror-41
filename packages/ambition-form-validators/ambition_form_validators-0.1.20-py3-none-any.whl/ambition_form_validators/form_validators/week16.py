from edc_constants.constants import YES
from edc_form_validators import FormValidator


class Week16FormValidator(FormValidator):
    def clean(self):
        self.applicable_if(
            YES, field="patient_alive", field_applicable="activities_help"
        )

        self.applicable_if(
            YES, field="patient_alive", field_applicable="illness_problems"
        )

        self.required_if(YES, field="patient_alive", field_required="rankin_score")
