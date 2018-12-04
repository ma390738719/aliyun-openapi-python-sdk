# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateBlockchainApplyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateBlockchainApply')

	def get_Size(self):
		return self.get_body_params().get('Size')

	def set_Size(self,Size):
		self.add_body_params('Size', Size)

	def get_MachineNum(self):
		return self.get_body_params().get('MachineNum')

	def set_MachineNum(self,MachineNum):
		self.add_body_params('MachineNum', MachineNum)

	def get_LiveTime(self):
		return self.get_body_params().get('LiveTime')

	def set_LiveTime(self,LiveTime):
		self.add_body_params('LiveTime', LiveTime)

	def get_Bizid(self):
		return self.get_body_params().get('Bizid')

	def set_Bizid(self,Bizid):
		self.add_body_params('Bizid', Bizid)