======================
Firefox Device Manager
======================

The device manager associates a Firefox Account with a user's "Foxes:" Firefox
OS, Android, iOS, and Desktop. The service allows Firefox clients to register
themselves, and exposes an API for other services to query an authenticated
user's devices. During registration, the device specifies its name and type, as
well as a push endpoint for other services to address it. This may be extended
to support individual applications on the device, which will allow services to
send broadcast and multicast push messages. The device manager also provides a
remote 'forget' mechanism that allows a user to invalidate a session on a lost
or stolen device.

The Firefox client ("device") API requires an OAuth bearer token issued by
Firefox Accounts for registration, and will be assigned a unique client-id that
must be stored on the client. The client should also register an endpoint for
itself and update the Push endpoint if/when it changes.

Registration API
================

All API points require an OAuth Bearer token in the ``Authentication`` header
field.

.. http:post:: /device
   :synopsis: Register a new device

   :json name: User-friendly device name.
   :json endpoint: (Optional) Endpoint to store.
   :resjson device-kd: UUID of the device registration.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json

.. http:get:: /device
   :synopsis: Get a list of all registered devices.

   :resheader Content-Type: application/json
   :resjson devices: List of registered devices, their names, uuid's, and
                     their push endpoints.

.. http:patch:: /device/(uuid:device_id)
   :synopsis: Update the Push endpoint or add token hashes for the device.

   :json endpoint: (Optional) New Push Endpoint.
   :json token_hashes: (Optional) Add list of token hash.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json

.. http:delete:: /device/(uuid:device_id)
   :synopsis: Delete a device

   This method requires an OAuth token issued within the last 5 minutes.
