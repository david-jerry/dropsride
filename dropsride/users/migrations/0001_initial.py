# Generated by Django 4.0.10 on 2023-04-22 23:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import dropsride.utils.validators
import model_utils.fields
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Middle Name')),
                ('unique_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Registration number')),
                ('ref_number', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Referral Code')),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE'), ('LGBQ', 'LGBQ')], default='LGBQ', max_length=10, verbose_name='Gender')),
                ('is_driver', models.BooleanField(db_index=True, default=False, verbose_name='Driver?')),
                ('is_verified', models.BooleanField(db_index=True, default=False, verbose_name='Verified?')),
                ('gave_consent', models.BooleanField(default=True, help_text="Share my registration data with dropsride's content providers for marketing purposes. This confirms you are up to the legal age approved in your country.", verbose_name='Privacy Consent')),
                ('customer_code', models.CharField(blank=True, max_length=500, null=True)),
                ('longitude', models.FloatField(default=0.0, verbose_name='User Longitude')),
                ('latitude', models.FloatField(default=0.0, verbose_name='User Latitude')),
                ('on_a_ride', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommender', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User Account',
                'verbose_name_plural': 'User Accounts',
                'ordering': ['-date_joined'],
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('old_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('margin', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('profit', models.BooleanField(default=True)),
                ('currency', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='currency.currency', verbose_name='Wallet Currency')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Wallet',
                'verbose_name_plural': 'User Wallets',
                'ordering': ['-modified'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VerifiedDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('license', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Drivers License')),
                ('license_exp', models.DateField(blank=True, null=True)),
                ('proof_of_ownership', models.FileField(blank=True, null=True, upload_to='document/proof_of_ownership', validators=[dropsride.utils.validators.validate_uploaded_pdf_extension])),
                ('vehicle_license', models.FileField(blank=True, null=True, upload_to='document/vehicle_license', validators=[dropsride.utils.validators.validate_uploaded_pdf_extension])),
                ('autocheck_certificate', models.FileField(blank=True, null=True, upload_to='document/autocheck_certificate', validators=[dropsride.utils.validators.validate_uploaded_pdf_extension])),
                ('insurance', models.FileField(blank=True, null=True, upload_to='document/insurance', validators=[dropsride.utils.validators.validate_uploaded_pdf_extension])),
                ('document_verified', models.BooleanField(default=False, verbose_name='Documents has been verified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Verified Documents',
                'verbose_name_plural': 'User Verified Documents',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email_notification', models.BooleanField(default=True)),
                ('push_notification', models.BooleanField(default=True)),
                ('sms_notification', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Setting',
                'verbose_name_plural': 'User Settings',
                'ordering': ['-modified'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SavedCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name_on_card', models.CharField(max_length=255)),
                ('card_no', models.CharField(db_index=True, max_length=26)),
                ('cvv', models.CharField(blank=True, max_length=5, null=True)),
                ('card_exp_month', models.CharField(blank=True, max_length=2)),
                ('card_exp_year', models.CharField(blank=True, max_length=4)),
                ('card_provider', models.CharField(default='master', max_length=40)),
                ('authorization_code', models.CharField(blank=True, max_length=500, null=True)),
                ('active', models.BooleanField(default=False)),
                ('card_verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_card', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Saved Card',
                'verbose_name_plural': 'User Saved Cards',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RegisteredVehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('vehicle_manufacturer', models.CharField(blank=True, max_length=500, verbose_name='Vehicle Make')),
                ('vehicle_plate_no', models.CharField(blank=True, max_length=500, verbose_name='Vehicle Plate Number')),
                ('vehicle_color', models.CharField(blank=True, max_length=500, verbose_name='Vehicle Plate Number')),
                ('active', models.BooleanField(default=False)),
                ('vehicle_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to=settings.AUTH_USER_MODEL)),
                ('vehicle_type', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_type', to='settings.cartype')),
            ],
            options={
                'verbose_name': 'Users Vehicle',
                'verbose_name_plural': 'Users Vehicles',
                'ordering': ['-modified'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReferralBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ref_bonus', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Referral Bonus',
                'verbose_name_plural': 'User Referral Bonuses',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='user/passport', verbose_name='Display Photo')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Customer Contact')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('bvn', models.CharField(blank=True, max_length=12, verbose_name='Bank Verification Number')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Customer Address')),
                ('town', models.CharField(blank=True, max_length=120, null=True, verbose_name='Customer Town/City')),
                ('county', models.CharField(blank=True, max_length=120, null=True, verbose_name='Customer County')),
                ('state', models.CharField(blank=True, max_length=120, null=True, verbose_name='Customer State')),
                ('post_code', models.CharField(blank=True, max_length=120, null=True, verbose_name='Customer Post Code')),
                ('country', models.CharField(blank=True, max_length=120, null=True, verbose_name='Customer Country')),
                ('profile_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Customer Contact')),
                ('bvn', models.CharField(blank=True, max_length=12, verbose_name='Bank Verification Number')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Kin Address')),
                ('town', models.CharField(blank=True, max_length=120, null=True, verbose_name='Kin Town/City')),
                ('county', models.CharField(blank=True, max_length=120, null=True, verbose_name='Kin County')),
                ('state', models.CharField(blank=True, max_length=120, null=True, verbose_name='Kin State')),
                ('post_code', models.CharField(blank=True, max_length=120, null=True, verbose_name='Kin Post Code')),
                ('country', models.CharField(blank=True, max_length=120, null=True, verbose_name='Kin Country')),
                ('longitude', models.FloatField(default=0.0, verbose_name='Kin Longitude')),
                ('latitude', models.FloatField(default=0.0, verbose_name='Kin Latitude')),
                ('gave_consent', models.BooleanField(default=False, verbose_name='Next of Kin has given consent to vouch for you')),
                ('kin_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nok', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Next Of Kin',
                'verbose_name_plural': 'User Next Of Kin',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('acc_no', models.CharField(db_index=True, max_length=17)),
                ('acc_name', models.CharField(max_length=255)),
                ('bank_verified', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_account', to='currency.banks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Saved Bank',
                'verbose_name_plural': 'User Saved Banks',
                'ordering': ['-modified'],
                'managed': True,
            },
        ),
    ]
