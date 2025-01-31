from import_export import resources


class CustomBaseModelResource(resources.ModelResource):
    def __init__(self, **kwargs):
        if "queryset" in kwargs:
            self.queryset = kwargs.pop("queryset")
        super().__init__(**kwargs)
        self.allowed_fields = kwargs.get(
            "allowed_fields",
        )

    def get_queryset(self):
        if hasattr(self, "queryset"):
            return self.queryset
        return super().get_queryset()
