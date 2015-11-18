from django_pg import models


class Office(models.Model):
    """Store data associated with Office entity"""
    # field 'location' in SSE
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "Office {} ({} , {})".format(self.name, self.city, self.coutry)


class Floor(models.Model):
    """
    Store data associated with Floor entity: floor plan, floor number
    Related to model: 'plan_editor.Office'
    """
    plan = models.ImageField()
    office = models.ForeignKey(Office)
    number = models.IntegerField()

    def __str__(self):
        return "Floor {}".format(self.number)


class Room(models.Model):
    """
    Store data associated with Room entity: coordinates, room number
    Related to model: 'plan_editor.Floor'
    """
    coordinates = models.JSONField()
    floor = models.ForeignKey(Floor)
    number = models.IntegerField()

    def __str__(self):
        return "Room {}".format(self.room)


class Workplace(models.Model):
    """
    Store data associated with Workplace entity: coordinates, workplace number,
    status.
    Related to model: 'plan_editor.Room'
    """
    coordinates = models.JSONField()
    room = models.ForeignKey(Room)
    number = models.IntegerField()
    # field for "waiting" and for "permanent", waiting for SSE update
    status = models.BooleanField()

    def __str__(self):
        return "Workplace {}".format(self.workplace)
