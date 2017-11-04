from swampdragon.serializers.model_serializer import ModelSerializer


class RealEditorSerializer(ModelSerializer):
    class Meta:
        model = 'calculation.RealEditor'
        publish_fields = ['editor_text','message']
