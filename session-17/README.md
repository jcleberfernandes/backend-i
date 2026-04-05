# Session 17 | Authentication and Permissions

## Objective
Apply basic access control using Django's built-in authentication system.

## Official References
- Django auth: https://docs.djangoproject.com/en/stable/topics/auth/
- Django permissions: https://docs.djangoproject.com/en/stable/topics/auth/default/

## Tutorial

### 1. Create Groups and Permissions
```bash
cd backend_i_django
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
```

In shell:
```python
from meetings.auth_demo import demo_auth
demo_auth()
```

Or use the management command:
```bash
python manage.py create_groups
```

### 2. Verify Permissions
In shell:
```python
from django.contrib.auth.models import User, Group, Permission

# Check user permissions
user = User.objects.get(username="editor")
print(user.get_all_permissions())

# Check group permissions
group = Group.objects.get(name="Editors")
print(group.permissions.all())
```

### 3. Test Login/Logout
```bash
python manage.py runserver
```
Visit:
- http://127.0.0.1:8000/admin/ - Login required
- http://127.0.0.1:8000/accounts/login/ - Login page
- http://127.0.0.1:8000/accounts/logout/ - Logout

### 4. View-based Permissions
```python
# Using decorators in views
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def meeting_list(request):
    # Only logged-in users can access
    pass

@permission_required("meetings.can_view_meeting", raise_exception=True)
def meeting_detail(request, pk):
    # Only users with permission can access
    pass
```

## Exercise
1. Create a new user "viewer" with only view permissions
2. Test that viewer cannot edit or delete meetings
3. Create a custom permission for "can_create_meeting"

## Challenge
Implement row-level permissions where users can only see their own meetings.
