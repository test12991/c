# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from qrl.generated import qrl_pb2 as qrl__pb2


class PublicAPIStub(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Public API used by clients (wallet/cli/etc)
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetNodeState = channel.unary_unary(
        '/qrl.PublicAPI/GetNodeState',
        request_serializer=qrl__pb2.GetNodeStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetNodeStateResp.FromString,
        )
    self.GetKnownPeers = channel.unary_unary(
        '/qrl.PublicAPI/GetKnownPeers',
        request_serializer=qrl__pb2.GetKnownPeersReq.SerializeToString,
        response_deserializer=qrl__pb2.GetKnownPeersResp.FromString,
        )
    self.GetPeersStat = channel.unary_unary(
        '/qrl.PublicAPI/GetPeersStat',
        request_serializer=qrl__pb2.GetPeersStatReq.SerializeToString,
        response_deserializer=qrl__pb2.GetPeersStatResp.FromString,
        )
    self.GetStats = channel.unary_unary(
        '/qrl.PublicAPI/GetStats',
        request_serializer=qrl__pb2.GetStatsReq.SerializeToString,
        response_deserializer=qrl__pb2.GetStatsResp.FromString,
        )
    self.GetAddressState = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressState',
        request_serializer=qrl__pb2.GetAddressStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressStateResp.FromString,
        )
    self.GetOptimizedAddressState = channel.unary_unary(
        '/qrl.PublicAPI/GetOptimizedAddressState',
        request_serializer=qrl__pb2.GetAddressStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetOptimizedAddressStateResp.FromString,
        )
    self.GetMultiSigAddressState = channel.unary_unary(
        '/qrl.PublicAPI/GetMultiSigAddressState',
        request_serializer=qrl__pb2.GetMultiSigAddressStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetMultiSigAddressStateResp.FromString,
        )
    self.IsSlave = channel.unary_unary(
        '/qrl.PublicAPI/IsSlave',
        request_serializer=qrl__pb2.IsSlaveReq.SerializeToString,
        response_deserializer=qrl__pb2.IsSlaveResp.FromString,
        )
    self.GetObject = channel.unary_unary(
        '/qrl.PublicAPI/GetObject',
        request_serializer=qrl__pb2.GetObjectReq.SerializeToString,
        response_deserializer=qrl__pb2.GetObjectResp.FromString,
        )
    self.GetLatestData = channel.unary_unary(
        '/qrl.PublicAPI/GetLatestData',
        request_serializer=qrl__pb2.GetLatestDataReq.SerializeToString,
        response_deserializer=qrl__pb2.GetLatestDataResp.FromString,
        )
    self.PushTransaction = channel.unary_unary(
        '/qrl.PublicAPI/PushTransaction',
        request_serializer=qrl__pb2.PushTransactionReq.SerializeToString,
        response_deserializer=qrl__pb2.PushTransactionResp.FromString,
        )
    self.TransferCoins = channel.unary_unary(
        '/qrl.PublicAPI/TransferCoins',
        request_serializer=qrl__pb2.TransferCoinsReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.ParseAddress = channel.unary_unary(
        '/qrl.PublicAPI/ParseAddress',
        request_serializer=qrl__pb2.ParseAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.ParseAddressResp.FromString,
        )
    self.GetChainStats = channel.unary_unary(
        '/qrl.PublicAPI/GetChainStats',
        request_serializer=qrl__pb2.GetChainStatsReq.SerializeToString,
        response_deserializer=qrl__pb2.GetChainStatsResp.FromString,
        )
    self.GetAddressFromPK = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressFromPK',
        request_serializer=qrl__pb2.GetAddressFromPKReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressFromPKResp.FromString,
        )
    self.GetMultiSigCreateTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetMultiSigCreateTxn',
        request_serializer=qrl__pb2.MultiSigCreateTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetMultiSigSpendTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetMultiSigSpendTxn',
        request_serializer=qrl__pb2.MultiSigSpendTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetMultiSigVoteTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetMultiSigVoteTxn',
        request_serializer=qrl__pb2.MultiSigVoteTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetMessageTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetMessageTxn',
        request_serializer=qrl__pb2.MessageTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetTokenTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetTokenTxn',
        request_serializer=qrl__pb2.TokenTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetTransferTokenTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetTransferTokenTxn',
        request_serializer=qrl__pb2.TransferTokenTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetSlaveTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetSlaveTxn',
        request_serializer=qrl__pb2.SlaveTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetLatticeTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetLatticeTxn',
        request_serializer=qrl__pb2.LatticeTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetTransaction = channel.unary_unary(
        '/qrl.PublicAPI/GetTransaction',
        request_serializer=qrl__pb2.GetTransactionReq.SerializeToString,
        response_deserializer=qrl__pb2.GetTransactionResp.FromString,
        )
    self.GetMiniTransactionsByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetMiniTransactionsByAddress',
        request_serializer=qrl__pb2.GetMiniTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetMiniTransactionsByAddressResp.FromString,
        )
    self.GetTransactionsByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetTransactionsByAddress',
        request_serializer=qrl__pb2.GetTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetTransactionsByAddressResp.FromString,
        )
    self.GetTokensByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetTokensByAddress',
        request_serializer=qrl__pb2.GetTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetTokensByAddressResp.FromString,
        )
    self.GetSlavesByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetSlavesByAddress',
        request_serializer=qrl__pb2.GetTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetSlavesByAddressResp.FromString,
        )
    self.GetLatticePKsByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetLatticePKsByAddress',
        request_serializer=qrl__pb2.GetTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetLatticePKsByAddressResp.FromString,
        )
    self.GetMultiSigAddressesByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetMultiSigAddressesByAddress',
        request_serializer=qrl__pb2.GetTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetMultiSigAddressesByAddressResp.FromString,
        )
    self.GetMultiSigSpendTxsByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetMultiSigSpendTxsByAddress',
        request_serializer=qrl__pb2.GetMultiSigSpendTxsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetMultiSigSpendTxsByAddressResp.FromString,
        )
    self.GetVoteStats = channel.unary_unary(
        '/qrl.PublicAPI/GetVoteStats',
        request_serializer=qrl__pb2.GetVoteStatsReq.SerializeToString,
        response_deserializer=qrl__pb2.GetVoteStatsResp.FromString,
        )
    self.GetInboxMessagesByAddress = channel.unary_unary(
        '/qrl.PublicAPI/GetInboxMessagesByAddress',
        request_serializer=qrl__pb2.GetTransactionsByAddressReq.SerializeToString,
        response_deserializer=qrl__pb2.GetInboxMessagesByAddressResp.FromString,
        )
    self.GetBalance = channel.unary_unary(
        '/qrl.PublicAPI/GetBalance',
        request_serializer=qrl__pb2.GetBalanceReq.SerializeToString,
        response_deserializer=qrl__pb2.GetBalanceResp.FromString,
        )
    self.GetTotalBalance = channel.unary_unary(
        '/qrl.PublicAPI/GetTotalBalance',
        request_serializer=qrl__pb2.GetTotalBalanceReq.SerializeToString,
        response_deserializer=qrl__pb2.GetTotalBalanceResp.FromString,
        )
    self.GetOTS = channel.unary_unary(
        '/qrl.PublicAPI/GetOTS',
        request_serializer=qrl__pb2.GetOTSReq.SerializeToString,
        response_deserializer=qrl__pb2.GetOTSResp.FromString,
        )
    self.GetHeight = channel.unary_unary(
        '/qrl.PublicAPI/GetHeight',
        request_serializer=qrl__pb2.GetHeightReq.SerializeToString,
        response_deserializer=qrl__pb2.GetHeightResp.FromString,
        )
    self.GetBlock = channel.unary_unary(
        '/qrl.PublicAPI/GetBlock',
        request_serializer=qrl__pb2.GetBlockReq.SerializeToString,
        response_deserializer=qrl__pb2.GetBlockResp.FromString,
        )
    self.GetBlockByNumber = channel.unary_unary(
        '/qrl.PublicAPI/GetBlockByNumber',
        request_serializer=qrl__pb2.GetBlockByNumberReq.SerializeToString,
        response_deserializer=qrl__pb2.GetBlockByNumberResp.FromString,
        )


class PublicAPIServicer(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Public API used by clients (wallet/cli/etc)
  """

  def GetNodeState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKnownPeers(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPeersStat(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStats(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOptimizedAddressState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultiSigAddressState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsSlave(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObject(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestData(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransferCoins(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ParseAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChainStats(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressFromPK(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultiSigCreateTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultiSigSpendTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultiSigVoteTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMessageTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTokenTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransferTokenTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSlaveTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatticeTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMiniTransactionsByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactionsByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTokensByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSlavesByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatticePKsByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultiSigAddressesByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMultiSigSpendTxsByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVoteStats(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInboxMessagesByAddress(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBalance(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTotalBalance(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOTS(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHeight(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlock(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlockByNumber(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublicAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetNodeState': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeState,
          request_deserializer=qrl__pb2.GetNodeStateReq.FromString,
          response_serializer=qrl__pb2.GetNodeStateResp.SerializeToString,
      ),
      'GetKnownPeers': grpc.unary_unary_rpc_method_handler(
          servicer.GetKnownPeers,
          request_deserializer=qrl__pb2.GetKnownPeersReq.FromString,
          response_serializer=qrl__pb2.GetKnownPeersResp.SerializeToString,
      ),
      'GetPeersStat': grpc.unary_unary_rpc_method_handler(
          servicer.GetPeersStat,
          request_deserializer=qrl__pb2.GetPeersStatReq.FromString,
          response_serializer=qrl__pb2.GetPeersStatResp.SerializeToString,
      ),
      'GetStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetStats,
          request_deserializer=qrl__pb2.GetStatsReq.FromString,
          response_serializer=qrl__pb2.GetStatsResp.SerializeToString,
      ),
      'GetAddressState': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressState,
          request_deserializer=qrl__pb2.GetAddressStateReq.FromString,
          response_serializer=qrl__pb2.GetAddressStateResp.SerializeToString,
      ),
      'GetOptimizedAddressState': grpc.unary_unary_rpc_method_handler(
          servicer.GetOptimizedAddressState,
          request_deserializer=qrl__pb2.GetAddressStateReq.FromString,
          response_serializer=qrl__pb2.GetOptimizedAddressStateResp.SerializeToString,
      ),
      'GetMultiSigAddressState': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultiSigAddressState,
          request_deserializer=qrl__pb2.GetMultiSigAddressStateReq.FromString,
          response_serializer=qrl__pb2.GetMultiSigAddressStateResp.SerializeToString,
      ),
      'IsSlave': grpc.unary_unary_rpc_method_handler(
          servicer.IsSlave,
          request_deserializer=qrl__pb2.IsSlaveReq.FromString,
          response_serializer=qrl__pb2.IsSlaveResp.SerializeToString,
      ),
      'GetObject': grpc.unary_unary_rpc_method_handler(
          servicer.GetObject,
          request_deserializer=qrl__pb2.GetObjectReq.FromString,
          response_serializer=qrl__pb2.GetObjectResp.SerializeToString,
      ),
      'GetLatestData': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestData,
          request_deserializer=qrl__pb2.GetLatestDataReq.FromString,
          response_serializer=qrl__pb2.GetLatestDataResp.SerializeToString,
      ),
      'PushTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.PushTransaction,
          request_deserializer=qrl__pb2.PushTransactionReq.FromString,
          response_serializer=qrl__pb2.PushTransactionResp.SerializeToString,
      ),
      'TransferCoins': grpc.unary_unary_rpc_method_handler(
          servicer.TransferCoins,
          request_deserializer=qrl__pb2.TransferCoinsReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'ParseAddress': grpc.unary_unary_rpc_method_handler(
          servicer.ParseAddress,
          request_deserializer=qrl__pb2.ParseAddressReq.FromString,
          response_serializer=qrl__pb2.ParseAddressResp.SerializeToString,
      ),
      'GetChainStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetChainStats,
          request_deserializer=qrl__pb2.GetChainStatsReq.FromString,
          response_serializer=qrl__pb2.GetChainStatsResp.SerializeToString,
      ),
      'GetAddressFromPK': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressFromPK,
          request_deserializer=qrl__pb2.GetAddressFromPKReq.FromString,
          response_serializer=qrl__pb2.GetAddressFromPKResp.SerializeToString,
      ),
      'GetMultiSigCreateTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultiSigCreateTxn,
          request_deserializer=qrl__pb2.MultiSigCreateTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetMultiSigSpendTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultiSigSpendTxn,
          request_deserializer=qrl__pb2.MultiSigSpendTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetMultiSigVoteTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultiSigVoteTxn,
          request_deserializer=qrl__pb2.MultiSigVoteTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetMessageTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetMessageTxn,
          request_deserializer=qrl__pb2.MessageTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetTokenTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetTokenTxn,
          request_deserializer=qrl__pb2.TokenTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetTransferTokenTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransferTokenTxn,
          request_deserializer=qrl__pb2.TransferTokenTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetSlaveTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlaveTxn,
          request_deserializer=qrl__pb2.SlaveTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetLatticeTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatticeTxn,
          request_deserializer=qrl__pb2.LatticeTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransaction,
          request_deserializer=qrl__pb2.GetTransactionReq.FromString,
          response_serializer=qrl__pb2.GetTransactionResp.SerializeToString,
      ),
      'GetMiniTransactionsByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetMiniTransactionsByAddress,
          request_deserializer=qrl__pb2.GetMiniTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetMiniTransactionsByAddressResp.SerializeToString,
      ),
      'GetTransactionsByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactionsByAddress,
          request_deserializer=qrl__pb2.GetTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetTransactionsByAddressResp.SerializeToString,
      ),
      'GetTokensByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetTokensByAddress,
          request_deserializer=qrl__pb2.GetTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetTokensByAddressResp.SerializeToString,
      ),
      'GetSlavesByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlavesByAddress,
          request_deserializer=qrl__pb2.GetTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetSlavesByAddressResp.SerializeToString,
      ),
      'GetLatticePKsByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatticePKsByAddress,
          request_deserializer=qrl__pb2.GetTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetLatticePKsByAddressResp.SerializeToString,
      ),
      'GetMultiSigAddressesByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultiSigAddressesByAddress,
          request_deserializer=qrl__pb2.GetTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetMultiSigAddressesByAddressResp.SerializeToString,
      ),
      'GetMultiSigSpendTxsByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetMultiSigSpendTxsByAddress,
          request_deserializer=qrl__pb2.GetMultiSigSpendTxsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetMultiSigSpendTxsByAddressResp.SerializeToString,
      ),
      'GetVoteStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetVoteStats,
          request_deserializer=qrl__pb2.GetVoteStatsReq.FromString,
          response_serializer=qrl__pb2.GetVoteStatsResp.SerializeToString,
      ),
      'GetInboxMessagesByAddress': grpc.unary_unary_rpc_method_handler(
          servicer.GetInboxMessagesByAddress,
          request_deserializer=qrl__pb2.GetTransactionsByAddressReq.FromString,
          response_serializer=qrl__pb2.GetInboxMessagesByAddressResp.SerializeToString,
      ),
      'GetBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetBalance,
          request_deserializer=qrl__pb2.GetBalanceReq.FromString,
          response_serializer=qrl__pb2.GetBalanceResp.SerializeToString,
      ),
      'GetTotalBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetTotalBalance,
          request_deserializer=qrl__pb2.GetTotalBalanceReq.FromString,
          response_serializer=qrl__pb2.GetTotalBalanceResp.SerializeToString,
      ),
      'GetOTS': grpc.unary_unary_rpc_method_handler(
          servicer.GetOTS,
          request_deserializer=qrl__pb2.GetOTSReq.FromString,
          response_serializer=qrl__pb2.GetOTSResp.SerializeToString,
      ),
      'GetHeight': grpc.unary_unary_rpc_method_handler(
          servicer.GetHeight,
          request_deserializer=qrl__pb2.GetHeightReq.FromString,
          response_serializer=qrl__pb2.GetHeightResp.SerializeToString,
      ),
      'GetBlock': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlock,
          request_deserializer=qrl__pb2.GetBlockReq.FromString,
          response_serializer=qrl__pb2.GetBlockResp.SerializeToString,
      ),
      'GetBlockByNumber': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlockByNumber,
          request_deserializer=qrl__pb2.GetBlockByNumberReq.FromString,
          response_serializer=qrl__pb2.GetBlockByNumberResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.PublicAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AdminAPIStub(object):
  """This is a place holder for testing/instrumentation APIs
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """


class AdminAPIServicer(object):
  """This is a place holder for testing/instrumentation APIs
  """


def add_AdminAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.AdminAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
