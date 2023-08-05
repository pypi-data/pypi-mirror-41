# Django PgQueue

The project was initially forked from [django-postgres-queue][dpq] for internal use
in some of my projects. After some changes and refactoring, writing tests, adding features such as warm shutdown I decided to put in on github and pypi as a
standalone package.

## Pros and cons

- You don't need any additional requirements such as Redis or RabbitMQ.
-

## Usage

```
pip install django-pgqueue
```

Then add `pqueue` into `INSTALLED_APPS`. Run `manage.py migrate` to create the jobs table.

Instantiate a queue object. This can go wherever you like and be called whatever
you like. For example, `someapp/queue.py`:

```
from pqueue.queue import Queue


def say_hello(queue, job):
    name = job.kwargs['name']
    print('Hello, {}!'.format(name))


task_queue = Queue(
    tasks={
        'say_hello': say_hello,
    },
    notify_channel='someapp_task_queue',
)
```

`someapp/management/commands/pgqueue_worker.py`

```
from pgqueue.worker import WorkerCommand
from someapp.queue import task_queue


class Command(WorkerCommand):
    queue = task_queue
```

```
from someapp.queue import task_queue

task_queue.enqueue('say_hello', {'name': 'Django'})
```

Please note that you can pass only primitives into job’s arguments as they are stored
as JSON in the database. When you try to pass any complex non-json-serializeable object,
you will get an error saying `<ObjectName> is not json serializable`.

## Periodic tasks

There is no built in way to run jobs periodically like a `celerybeat` in Celery.
But you still can use cron. For example you can create a universal command
to execute any task. Something like that:

```
import json

from django.core.management import BaseCommand
from someapp.queue import task_queue


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('task_name')
        parser.add_argument('task_kwargs')

    def handle(self, task_name, task_kwargs, **options):
        task_queue.enqueue(task_name, json.loads(task_kwargs))
```

And then put it into your cron records:

```
0 0 * * *  /path/to/python manage.py run_task say_hello '{"name": "Django!"}'
```


[dpq]: https://github.com/gavinwahl/django-postgres-queue
