# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.28
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SimWordEntityExtractorInstanceDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'long_name': 'str',
        'desc': 'str',
        'similar_words': 'list[str]',
        'threshold': 'float',
        'word_manifold': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'long_name': 'long_name',
        'desc': 'desc',
        'similar_words': 'similar_words',
        'threshold': 'threshold',
        'word_manifold': 'word_manifold'
    }

    def __init__(self, name=None, id=None, long_name=None, desc=None, similar_words=None, threshold=None, word_manifold=None):  # noqa: E501
        """SimWordEntityExtractorInstanceDetail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._long_name = None
        self._desc = None
        self._similar_words = None
        self._threshold = None
        self._word_manifold = None
        self.discriminator = None

        self.name = name
        self.id = id
        if long_name is not None:
            self.long_name = long_name
        if desc is not None:
            self.desc = desc
        self.similar_words = similar_words
        self.threshold = threshold
        self.word_manifold = word_manifold

    @property
    def name(self):
        """Gets the name of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimWordEntityExtractorInstanceDetail.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The unique id of a specific version of the model instance.  # noqa: E501

        :return: The id of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimWordEntityExtractorInstanceDetail.

        The unique id of a specific version of the model instance.  # noqa: E501

        :param id: The id of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def long_name(self):
        """Gets the long_name of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The human-friendly-name of the instance.  # noqa: E501

        :return: The long_name of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this SimWordEntityExtractorInstanceDetail.

        The human-friendly-name of the instance.  # noqa: E501

        :param long_name: The long_name of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def desc(self):
        """Gets the desc of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this SimWordEntityExtractorInstanceDetail.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def similar_words(self):
        """Gets the similar_words of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The list of similar words to test against.  # noqa: E501

        :return: The similar_words of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._similar_words

    @similar_words.setter
    def similar_words(self, similar_words):
        """Sets the similar_words of this SimWordEntityExtractorInstanceDetail.

        The list of similar words to test against.  # noqa: E501

        :param similar_words: The similar_words of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: list[str]
        """
        if similar_words is None:
            raise ValueError("Invalid value for `similar_words`, must not be `None`")  # noqa: E501

        self._similar_words = similar_words

    @property
    def threshold(self):
        """Gets the threshold of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The threshold below which words are not similar.  # noqa: E501

        :return: The threshold of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this SimWordEntityExtractorInstanceDetail.

        The threshold below which words are not similar.  # noqa: E501

        :param threshold: The threshold of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: float
        """
        if threshold is None:
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold

    @property
    def word_manifold(self):
        """Gets the word_manifold of this SimWordEntityExtractorInstanceDetail.  # noqa: E501

        The word manifold used to measure word similarity.  # noqa: E501

        :return: The word_manifold of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._word_manifold

    @word_manifold.setter
    def word_manifold(self, word_manifold):
        """Sets the word_manifold of this SimWordEntityExtractorInstanceDetail.

        The word manifold used to measure word similarity.  # noqa: E501

        :param word_manifold: The word_manifold of this SimWordEntityExtractorInstanceDetail.  # noqa: E501
        :type: str
        """
        if word_manifold is None:
            raise ValueError("Invalid value for `word_manifold`, must not be `None`")  # noqa: E501

        self._word_manifold = word_manifold

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SimWordEntityExtractorInstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
