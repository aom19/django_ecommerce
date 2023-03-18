
# Commands
## Generate random key
```bash
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```


## Create superuser
```bash
python manage.py createsuperuser
```

## Genereate schema
```bash
python3 manage.py spectacular --file schema.yml
```

##  Run Tests with coverage
```bash
coverage run -m pytest
```

