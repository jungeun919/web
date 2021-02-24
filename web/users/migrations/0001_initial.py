# Generated by Django 3.1.2 on 2021-02-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=20, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=128, null=True, unique=True, verbose_name='이메일')),
                ('hp', models.IntegerField(null=True, unique=True, verbose_name='핸드폰번호')),
                ('name', models.CharField(max_length=8, null=True, verbose_name='이름')),
                ('student_id', models.IntegerField(null=True, verbose_name='학번')),
                ('grade', models.CharField(choices=[('선택안함', '선택안함'), ('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('졸업생', '졸업생')], max_length=18, null=True, verbose_name='학년')),
                ('level', models.CharField(choices=[('3', 'Lv3_미인증사용자'), ('2', 'Lv2_인증사용자'), ('1', 'Lv1_관리자'), ('0', 'Lv0_개발자')], default=3, max_length=18, verbose_name='등급')),
                ('circles', models.CharField(choices=[], max_length=18, null=True, verbose_name='동아리')),
                ('department', models.CharField(choices=[], max_length=24, null=True, verbose_name='학과')),
                ('auth', models.CharField(max_length=10, null=True, verbose_name='인증번호')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': '회원목록',
            },
        ),
    ]
