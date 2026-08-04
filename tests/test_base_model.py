from backend.models.base import VCCBaseModel


def test_base_model_creation():
    model = VCCBaseModel()

    assert model.id is not None
    assert model.created_at is not None
    assert model.updated_at is not None
