from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    permissions = {
        'log_issue': Permission.objects.get(codename='log_issue'),
        'view_issue': Permission.objects.get(codename='view_issue'),
        'resolve_issue': Permission.objects.get(codename='resolve_issue'),
        'provide_feedback': Permission.objects.get(codename='provide_feedback'),
        'assign_issue': Permission.objects.get(codename='assign_issue'),
        'oversee_issue': Permission.objects.get(codename='oversee_issue'),
    }

    student_group, _=Group.objects.get_or_create(name='Students')
    student_permissions = [
        permissions['log_issue'],
        permissions['view_issue'],
    ]
    student_group.permissions.set(student_permissions)


    lecturer_group, _=Group.objects.get_or_create(name='Lecturers')
    lecturer_permissions = [
        permissions['view_issue'],
        permissions['resolve_issue'],
        permissions['provide_feedback'],
    ]
    lecturer_group.permissions.set(lecturer_permissions)


    registrar_group, _=Group.objects.get_or_create(name='Registrars')
    registrar_permissions = [
        permissions['view_issue'],
        permissions['oversee_issue'],
        permissions['assign_issue'],
    ]

    registrar_group.permissions.set(registrar_permissions)

def assign_users_to_groups(apps, schema_editor):
    User = apps.get_model('users','User')
    Group = apps.get_model('auth', 'Group')

    for user in User.objects.all():
        if user.role =='student':
            group = Group.objects.get(name='Students')
        elif user.role =='lecturer':
            group = Group.objects.get(name='Lecturers')
        elif user.role =='registrar':
            group = Group.objects.get(name='Registrars')
        user.groups.add(group)
        
class Migrations(migrations.Migration):
    dependencies  = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions),
        migrations.RunPython(assign_users_to_groups),
    ]