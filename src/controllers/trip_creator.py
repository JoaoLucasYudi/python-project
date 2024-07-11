import uuid

class TripCreator:
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> dict:
        try:
            emails = body.get('emails_to_invite')

            trip_id = str(uuid.uuid4())
            trips_infos = {**body, 'id': trip_id}

            self.__trip_repository.create_trip(trips_infos)

            if emails:
                for email in emails:
                    email_id = str(uuid.uuid4())
                    email_infos = {'id': email_id, 'trip_id': trip_id, 'email': email}
                    self.__emails_repository.registry_email(email_infos)

            return {
                'body': {'id': trip_id},
                'status_code': 201
            }

        except Exception as e:
            return {
                'body': {'error': 'Bad request', 'message': str(e)},
                'status_code': 400
            }
