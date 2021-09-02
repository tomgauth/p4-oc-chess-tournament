# This is the master controller
from views.master_view import MasterView


class MasterController:

    def sanitised_input(self, prompt='=>', type_=None, min_=None, max_=None,
                        len_min=None, len_max=None, range_=None, default=None):
        mv = MasterView()
        if min_ is not None and max_ is not None and max_ < min_:
            raise ValueError("min_ must be less than or equal to max_.")
        if len_min is not None and len_max is not None and len_max < len_min:
            raise ValueError("len_min must be less than or equal to len_max.")
        while True:
            ui = mv.get_input(prompt)

            if default is not None and ui == '':
                ui = default

            elif type_ is not None:
                try:
                    ui = type_(ui)
                except ValueError:
                    mv.custom_message(
                        "Input type must be {0}.".format(type_.__name__))
                    continue
            if max_ is not None and ui > max_:
                mv.custom_message(
                    "Input must be less than or equal to {0}.".format(max_))
            elif min_ is not None and ui < min_:
                mv.custom_message(
                    "Input must be greater than or equal to {0}.".format(
                        min_))
            elif len_max is not None and len(str(ui)) > len_max:
                mv.custom_message(
                    "Input length must be shorter than or equal to {0}."
                    .format(len_max))
            elif len_min is not None and len(str(ui)) < len_min:
                mv.custom_message(
                    "Input length must be longer than or equal to {0}."
                    .format(len_min))
            elif range_ is not None and ui not in range_:
                if isinstance(range_, range):
                    template = "Input must be between {0.start} and {0.stop}."
                    mv.custom_message(template.format(range_))
                else:
                    template = "Input must be {0}."
                    if len(range_) == 1:
                        mv.custom_message(template.format(*range_))
                    else:
                        expected = " or ".join((
                            ", ".join(str(x) for x in range_[:-1]),
                            str(range_[-1])
                        ))
                        mv.custom_message(template.format(expected))
            else:
                return ui
