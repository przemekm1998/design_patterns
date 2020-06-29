class AsDictionaryMixin:
    def to_dict(self):
        """
        Return representation as dictionary
        Create a dictionary mapping prop to value for each item in
        self.__dict__.items() if the prop is not internal.
        """

        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith('_')
