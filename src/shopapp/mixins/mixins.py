from django.urls import reverse


class ExtraContextMixin:
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContextMixin, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.object.pk})


class SuccessListUrlMixin:
    def get_success_url(self):
        return reverse(self.success_url, kwargs={})
