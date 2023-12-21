from django.shortcuts import redirect

def admin_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            # Redirect unauthorized users to login page or other appropriate page
            return redirect('admin/')  # You can replace 'login' with your login URL
        return view_func(request, *args, **kwargs)
    return wrapped_view