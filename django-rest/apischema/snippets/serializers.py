from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
#
#     """
#     PART 1: attributed being serialized
#     """
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#
#     """
#     Define how fledged instances are created or modified.
#     """
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

# Example: ModelSerializers
#
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username') # rouce: which argument to be populated in a view
#     # owner = serializers.CharField(read_only=True, source='owner.username') # same as line above
#     class Meta:
#         """
#         Make sure to add the reference key to the Meta.fields
#         """
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
#
#
# # Section authentication & permissions
#
#
# class UserSerializer(serializers.ModelSerializer):
#
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id','username','snippets')
#         # becuase snippets is a reverse relationship on the User model, it will not be
#         # included by default when using the ModelSerializer class... require explicit field

# Example : Hyperlinked APIs
"""
It does not include the id field by default.
It includes a url field, using HyperlinkedIdentityField.
Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
"""


class SnippetSerializer(serializers.HyperlinkedModelSerializer):  # its id is an url
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.\
        HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.\
        HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')