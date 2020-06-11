from freezegun import freeze_time

from src.domain.item import Item


class ItemTest:
    @freeze_time('2020-02-04')
    def should_return_false_when_season_calendar_is_false_for_current_month(self):
        # Given
        item = Item(
            identifier=12,
            name='Courgette',
            season_calendar=[True, False, True, True, True, True, True, True, True, True, True, True]
        )

        # When
        is_seasonal = item.is_seasonal()

        # Then
        assert not is_seasonal
