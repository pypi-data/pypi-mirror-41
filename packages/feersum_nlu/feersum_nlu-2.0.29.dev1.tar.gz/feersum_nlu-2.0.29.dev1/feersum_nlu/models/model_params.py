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


class ModelParams(object):
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
        'long_name': 'str',
        'desc': 'str',
        'threshold': 'float'
    }

    attribute_map = {
        'long_name': 'long_name',
        'desc': 'desc',
        'threshold': 'threshold'
    }

    def __init__(self, long_name=None, desc=None, threshold=None):  # noqa: E501
        """ModelParams - a model defined in Swagger"""  # noqa: E501

        self._long_name = None
        self._desc = None
        self._threshold = None
        self.discriminator = None

        if long_name is not None:
            self.long_name = long_name
        if desc is not None:
            self.desc = desc
        if threshold is not None:
            self.threshold = threshold

    @property
    def long_name(self):
        """Gets the long_name of this ModelParams.  # noqa: E501


        :return: The long_name of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this ModelParams.


        :param long_name: The long_name of this ModelParams.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def desc(self):
        """Gets the desc of this ModelParams.  # noqa: E501


        :return: The desc of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ModelParams.


        :param desc: The desc of this ModelParams.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def threshold(self):
        """Gets the threshold of this ModelParams.  # noqa: E501


        :return: The threshold of this ModelParams.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ModelParams.


        :param threshold: The threshold of this ModelParams.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

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
        if not isinstance(other, ModelParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
