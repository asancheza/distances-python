#!/usr/bin/python
# -*- coding: utf-8 -*- 

# Copyright (c) 2015 Alejandro Sanchez Acosta
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json, math

"""
Class Distance to calculate near users
"""
class Distance:
	"""
	Init distance with the nearUsers dictionary and earthRadius in kilometers
	"""
	def __init__(self):
		self.nearUsers = {}
		self.earthRadius = 6378.1370 

	""" 
	Calculate the distance in longitude and latitude from isNearHeadquarters
	"""
	def isNearHeadquarters(self, latitude, longitude, kilometers):
	  headquarterLatitude = 53.3381985
	  headquarterLongitude = -6.2592576

	  # Convert latitude and longitude
	  degreesToRadians = math.pi / 180.0
	  phi1 = (90 - headquarterLatitude) * degreesToRadians
	  phi2 = (90 - float(latitude)) * degreesToRadians

	  theta1 = headquarterLongitude * degreesToRadians
	  theta2 = float(longitude) * degreesToRadians
	  
	  # Calculate distance with arc and convert to kilometers
	  cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math.cos(phi2))
	  distance = math.acos( cos ) * self.earthRadius
	   
	  # Check distance is less or equal than 100 kms
	  if (distance <= kilometers):
	    return True

	  return False

	""" 
	Read file customers.txt and parse json lines
	"""
	def readFile(self):
		with open("customers.txt") as customers:
		  for customer in customers:
		    customerData = json.loads(customer)
		    # Check near places in 100 kilometers
		    if self.isNearHeadquarters(customerData["latitude"], customerData["longitude"], 100):
		      user_id = int(customerData['user_id'])
		      self.nearUsers[user_id] = customerData

	"""
	Print the stored near users in the dictionary sorted by user id
	"""
	def printNearUsers(self):
		keylist = self.nearUsers.keys()
		# Sort the keylist by user id ascending
		keylist.sort()
		for key in keylist:
			nearUsersData = self.nearUsers[key]
			print "User id:" + str(nearUsersData["user_id"]) + " Name:" + nearUsersData["name"]

""" 
Creates distance object, read file and print sorted results
"""
distance = Distance()
distance.readFile()
distance.printNearUsers()
