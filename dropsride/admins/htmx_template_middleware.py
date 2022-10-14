

# class HtmxResponseMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         return self.get_response(request)

#     def process_template_response(self, request, response):
#         app_name = resolve(request.path).app_name
#         if app_name in settings.HTMX_APPS:
#             response.template_name = f"{app_name}/{response.template_name[0]}"
#             if request.htmx:
#                 response.context_data["base_template"] = "partial.html"
#             else:
#                 response.context_data["base_template"] = "base.html"
#         return response
