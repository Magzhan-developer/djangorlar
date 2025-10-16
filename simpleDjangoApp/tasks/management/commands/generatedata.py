from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from random import choice
from typing import Any
from datetime import datetime

class Command(BaseCommand):
    
    EMAIL_DOMAINS = (
        "example.com",
        "test.com",
        "sample.org",
        "demo.net",
        "mail.com",
    )
    SOME_WORDS = (
        "lorem",
        "ipsum",
        "dolor",
        "sit",
        "amet",
        "consectetur",
        "adipiscing",
        "elit",
        "sed",
        "do",
        "eiusmod",
        "tempor",
        "incididunt",
        "ut",
        "labore",
        "et",
        "dolore",
        "magna",
        "aliqua",
    )
    
    def __generate_users(self,user_count:int = 20) -> None:
        """
        Generates users for testing purposes.
        """
        USER_PASSWORD = make_password('simplePass123')
        created_users :list[User] = []
        users_before = User.objects.count()
        for i in range(user_count):
            username:str = f'user_{i + 1}'
            email:str = f'user{i+1}@{choice(self.EMAIL_DOMAINS)}'
            created_users.append(
                User(
                    username=username,
                    email=email,
                    password=USER_PASSWORD,
                )
            )
        User.object.bulk_create(created_users, ignore_conflicts=True)
        users_after:int = User.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'created {users_after - users_before} users' 
            )
        )
        
    def handle(self,*args:tuple[Any, ...],**kwargs:dict[str,Any]) -> None:
        start_time: datetime = datetime.now()
        self.__generate_users() 
        
        self.stdout.write(
            "The whole process to generate data took: {} seconds".format(
                (datetime.now() - start_time).total_seconds()
            )
        )