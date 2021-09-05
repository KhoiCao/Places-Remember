from django.test import TestCase
from django.contrib.auth.models import User
from place.models import Memory
from django.urls import reverse

class MemoryTestCase(TestCase):
    fixtures = ["data.json"]

    def setUp(self):
        self.user = User.objects.get(pk=3)
        self.client.force_login(self.user, "django.contrib.auth.backends.ModelBackend")

    def test_memory_fetch(self):
        memories = Memory.objects.filter(owner=self.user)
        self.assertEqual(len(memories), 3)

    def test_memory_creation(self):
        prev_total_memories = Memory.objects.count()
        prev_user_num_memories = Memory.objects.filter(owner=self.user).count()
        new_memory = {
            "memory_name" : "Summer holiday 2020",
            "location" : "HCM City",
            "comment" : "Fun"
        }
        response = self.client.post(reverse("place-add"), new_memory)
        curr_total_memories = Memory.objects.count()
        curr_user_num_memories = Memory.objects.filter(owner=self.user).count()
        inserted_memory = Memory.objects.last()
        self.assertEqual(curr_total_memories - prev_total_memories, 1)
        self.assertEqual(curr_user_num_memories - prev_user_num_memories, 1)
        self.assertEqual(inserted_memory.memory_name, new_memory["memory_name"])
        self.assertEqual(inserted_memory.location, new_memory["location"])
        self.assertEqual(inserted_memory.comment, new_memory["comment"])
        self.assertRedirects(response, reverse("place-list"))
        