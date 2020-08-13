from django.db import models

ES_STATS_TYPES = (('node_stats', 'node_stats'),
                  ('cluster_stats', 'cluster_stats'))

# Create your models here.


class ClusterHost(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    host = models.CharField(max_length=100, null=False)
    port = models.IntegerField(default=9200)
    protocol = models.CharField(max_length=20, null=False, default='http')
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Cluster Host'
        verbose_name_plural = 'Cluster Hosts'

    def __str__(self):
        return "{}({})".format(self.name, self.host)


class Stats(models.Model):
    cluster_host = models.ForeignKey(ClusterHost,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, choices=ES_STATS_TYPES)

    request_date = models.DateTimeField(auto_now_add=True, blank=True)
    json_content = models.TextField(null=False)

    class Meta:
        unique_together = [['cluster_host_id', 'request_date', 'name']]
        indexes = [
            models.Index(fields=['-request_date', ]),
        ]

        verbose_name = 'Stats'
        verbose_name_plural = 'Stats'

    def __str__(self):
        return "{}({})".format(self.name, self.cluster_host)


class Settings(models.Model):
    key = models.CharField(max_length=200, primary_key=True)
    value = models.TextField(null=False)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return "{}={}".format(self.key, self.value)
