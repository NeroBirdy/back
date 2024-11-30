from datetime import date, datetime
from enum import Enum
from typing import Annotated, Any, Dict, List, Literal, Optional, Union
from pydantic import UUID4, BaseModel, EmailStr, Field, StringConstraints


class BodyLdapLoginAuthLdapLoginPost(BaseModel):
    login: str 
    password: str 
    fingerprint: Optional[Dict[str, Any]] 


class BodyLoginAuthLoginPost(BaseModel):
    login: str 
    password: str 
    fingerprint: Optional[Dict[str, Any]] 


class BodyUploadFileMeetingsAttachmentsPost(BaseModel):
    file: bytes 


class BuildingBare(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 
    address: Annotated[str, StringConstraints(min_length=1)]
    municipalAreaId: int 


class BuildingCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    address: Annotated[str, StringConstraints(min_length=1)]   
    municipalAreaId: int 


class BuildingList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[BuildingBare] 
    sortBy: Optional[str] 


class CatalogElementBare(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 


class CatalogElementCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 


class CiscoParticipantsLimitOut(BaseModel):
    current: int 
    max: int


class CiscoRoomBare(BaseModel):
    connectUrl: Optional[str]
    roomUri: Optional[str] 
    sipDomainUrl: Optional[str]    
    sipIpUrl: Optional[str]    
    callId: Optional[str]
    id: int 
    adminConnectUrl: Optional[str]
    adminAccessUri: Optional[str]


class CiscoRoomPublicBare(BaseModel):
    connectUrl: Optional[str]
    roomUri: Optional[str] 
    sipDomainUrl: Optional[str]    
    sipIpUrl: Optional[str]    
    callId: Optional[str]


class CiscoVCSSettingBare(BaseModel):
    isMicrophoneOn: bool 
    isVideoOn: bool 
    isWaitingRoomEnabled: bool 
    needVideoRecording: Optional[bool]
    id: int 
    isPrivateLicenceUsed: bool 


class CiscoVCSSettingCreate(BaseModel):
    isMicrophoneOn: bool 
    isVideoOn: bool 
    isWaitingRoomEnabled: bool 
    needVideoRecording: Optional[bool]


class CumulativeMeeting(BaseModel):
    date: date 
    count: int 


class CumulativeMeetings(BaseModel):
    data: List[CumulativeMeeting] 


class CumulativeType(Enum):
    meetings = 'meetings'
    users = 'users'


class DepartmentBare(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)]  
    shortName: str 
    address: Optional[str] 
    email: Optional[EmailStr] 
    parentId: Optional[int] 
    id: int 
    ldapName: Optional[str] 


class DepartmentBrief(BaseModel):
    id: int 
    name: str 
    shortName: str 
    parentId: Optional[int] 


class DepartmentFull(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)]    
    shortName: str 
    address: Optional[str] 
    email: Optional[EmailStr] 
    parentId: Optional[int] 
    id: int 
    ldapName: Optional[str] 
    createdAt: datetime 
    createdBy: Optional[int] 


class DepartmentList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[DepartmentBare] 
    sortBy: Optional[str] 


class DepartmentListBrief(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[DepartmentBrief] 
    sortBy: Optional[str] 


class DepartmentUpdate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)]    
    shortName: str 
    address: Annotated[str, StringConstraints(min_length=1)] 
    email: EmailStr 
    parentId: Optional[int] 


class EmailTemplateEditableFields(BaseModel):
    title: str 
    content: str 


class EmailTemplateOut(BaseModel):
    title: str 
    content: str 
    id: int 
    name: str 
    createdAt: Optional[datetime] 
    updatedAt: Optional[datetime] 


class EventBare(BaseModel):
    isOfflineEvent: bool 
    roomId: Optional[int] 
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)] 
    startedAt: datetime 
    endedAt: Optional[datetime]    
    duration: Annotated[Optional[int], Field(ge=10)]   
    id: int 


class EventCreate(BaseModel):
    isOfflineEvent: bool 
    roomId: Optional[int] 
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)] 
    startedAt: datetime 
    endedAt: Optional[datetime]    
    duration: Annotated[Optional[int], Field(ge=10)]  

class EventList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[EventBare] 
    sortBy: Optional[str] 


class EventRelativeStat(BaseModel):
    offline: float 
    online: float 


class EventTimeCollision(BaseModel):
    startedAt: datetime    
    endedAt: datetime    
    roomId: Optional[int] 


class ExternalVCSSettingCreate(BaseModel):
    externalUrl: str 
    permanentRoomId: Optional[int] 


class FileBare(BaseModel):
    name: Annotated[str, StringConstraints(max_length=256)] 
    id: UUID4 


class FileCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=256)] 


class GroupBare(BaseModel):
    id: int 
    name: Annotated[str, StringConstraints(min_length=3, max_length=256)] 
    description: Optional[Annotated[str, StringConstraints(max_length=2048)]] 
    params: Optional[Dict[str, Any]] 
    isPublic: Optional[bool] 
    copiedFromId: Optional[int] 
    membersCount: Optional[int] 
    createdBy: int 


class GroupList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[GroupBare] 
    sortBy: Optional[str] 


class GroupShareToken(BaseModel):
    token: str 
    expiresAt: datetime 


class IdMixin(BaseModel):
    id: int 


class MeetingBackend(Enum):
    cisco = 'cisco'
    permanentroom = 'permanentroom'
    external = 'external'
    vinteo = 'vinteo'


class MeetingLicenseThreshold(BaseModel):
    timeStart: str 
    timeEnd: str 
    value: int 


class MeetingLicenseUsedTime(BaseModel):
    timeStart: str 
    timeEnd: str 
    privateLicensesUsedCountRelative: Optional[float]    
    publicLicensesUsedCountRelative: Optional[float]

class MeetingLicenseUsedTimeList(BaseModel):
    data: List[MeetingLicenseUsedTime] 


class MeetingRecurrenceFrequency(Enum):
    int_0 = 0
    int_1 = 1
    int_2 = 2
    int_3 = 3
    int_4 = 4
    int_5 = 5
    int_6 = 6


class MeetingRecurrenceUpdateType(Enum):
    only = 'only'
    only_following = 'only_following'
    all = 'all'


class MeetingRecurrenceWeekday(Enum):
    int_0 = 0
    int_1 = 1
    int_2 = 2
    int_3 = 3
    int_4 = 4
    int_5 = 5
    int_6 = 6


class MeetingSortingFields(Enum):
    id = 'id'
    startedAt = 'startedAt'
    createdAt = 'createdAt'
    eventId = 'eventId'
    name = 'name'


class MeetingStates(Enum):
    booked = 'booked'
    cancelled = 'cancelled'
    started = 'started'
    ended = 'ended'


class MeetingTimeStat(BaseModel):
    average: float 
    min: float 
    max: float 
    sum: float 


class MeetingsCalendarList(BaseModel):
    data: List[date] 


class MeetingsTraffic(BaseModel):
    data: int 


class MunicipalAreaList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[CatalogElementBare] 
    sortBy: Optional[str] 


class ParticipantCreate(BaseModel):
    email: EmailStr 
    lastName: Optional[str] 
    firstName: Optional[str] 
    middleName: Optional[str] 


class ParticipantMock(BaseModel):
    id: int 


class ParticipantOut(BaseModel):
    id: int 
    email: EmailStr 
    lastName: Optional[str] 
    firstName: Optional[str] 
    middleName: Optional[str] 
    isApproved: Optional[bool]


class ParticipantsCollisionIn(BaseModel):
    startedAt: datetime    
    endedAt: Optional[datetime]    
    currentMeetingId: Optional[int]
    duration: Optional[int] 
    participants: Optional[List[ParticipantMock]] 
    groups: Optional[List[IdMixin]]


class PermanentRoomIn(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Optional[str]
    link: str 
    backend: Optional[MeetingBackend]


class PermanentRoomOut(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Optional[str]
    id: int 
    link: str 
    backend: Optional[MeetingBackend]
    createdAt: datetime 


class PrivateLicenseIn(BaseModel):
    email: EmailStr 


class PrivateLicenseOut(BaseModel):
    email: EmailStr 
    id: int 
    createdAt: datetime 


class RefreshTokenIn(BaseModel):
    token: str 


class RegisterUserIn(BaseModel):
    login: Annotated[str, StringConstraints(min_length=4)] 
    password: Annotated[str, StringConstraints(min_length=6)] 
    email: EmailStr 
    lastName: str 
    firstName: str 
    middleName: Optional[str] 
    phone: Optional[str] 
    birthday: Optional[date] 
    roleId: Literal[5] 
    type: Literal['native'] 


class ReportByDate(BaseModel):
    booked: int 
    cancelled: int 
    ended: int 
    started: int 
    total: int 
    date: date 


class ReportType(Enum):
    departments = 'departments'
    dates = 'dates'
    general = 'general'


class ResetPasswordConfirm(BaseModel):
    newPassword: Annotated[str, StringConstraints(min_length=6)] 
    resetToken: str 


class ResetPasswordIn(BaseModel):
    email: str 


class RoleBare(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 
    permissions: List[str] 


class RoleList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[RoleBare] 
    sortBy: Optional[str] 


class RoomCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    buildingId: int 
    maxParticipants: Annotated[Optional[int], Field(ge=2)]  
    isSkitNotified: Optional[bool]


class RoomShort(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 
    buildingId: int 
    maxParticipants: Annotated[Optional[int], Field(ge=2)]  
    isSkitNotified: Optional[bool]


class RoomStat(BaseModel):
    id: int 
    name: str 
    usedCount: int 


class RoomStatList(BaseModel):
    data: List[RoomStat] 


class SettingUpdate(BaseModel):
    backend: MeetingBackend    
    dropEndedConferenceAfter: int
    enableConferenceBefore: int
    maxParticipants: int
    maxConferences: int
    maxPrivateLicenseConferences: int
    callLegProfileForOrganizer: str
    privateLicenceOwnerJid: str


class SimpleUserBare(BaseModel):
    id: int 
    login: Optional[str] 
    lastName: Optional[str] 
    firstName: Optional[str] 
    middleName: Optional[str] 
    departmentId: Optional[int] 
    email: Optional[str] 


class SimpleUserCreate(BaseModel):
    firstName: str 
    lastName: str 
    middleName: Optional[str] 
    email: EmailStr 


class SimpleUserList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[SimpleUserBare] 
    sortBy: Optional[str] 


class StatusResponse(BaseModel):
    status: Optional[str] 
    warning: Optional[str] 
    warning_info: Optional[List[Dict[str, Any]]] 


class TemplateVariableDescriptionOut(BaseModel):
    templateName: str 
    name: str 
    description: str 


class TimeSystem(Enum):
    hours = 'hours'
    minutes = 'minutes'


class TopByOrganizedDepartments(BaseModel):
    count: int 
    department: DepartmentBrief


class UserBrief(BaseModel):
    id: int 
    lastName: Optional[str] 
    firstName: Optional[str] 
    middleName: Optional[str] 
    roleIds: List[int] 
    departmentId: Optional[int] 
    email: str 


class UserInfoOut(BaseModel):
    id: int 
    departmentId: Optional[int] 
    post: Optional[str] 
    permissions: Optional[List[str]] 
    login: Optional[str] 
    email: EmailStr 
    lastName: str 
    firstName: str 
    middleName: Optional[str] 
    birthday: Optional[date] 
    phone: Optional[str] 
    updatedAt: datetime 
    priority: Optional[int] 
    roles: List[RoleBare] 
    department: Optional[DepartmentBare] = None


class UserListBrief(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[UserBrief] 
    sortBy: Optional[str] 


class UserMeetings(BaseModel):
    user: UserBrief
    meetingsCount: int 


class UserMeetingsList(BaseModel):
    data: List[UserMeetings] 


class UserPriority(Enum):
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3


class UserSelfUpdateInfo(BaseModel):
    password: Optional[Annotated[str, StringConstraints(min_length=6)]] 
    firstName: str 
    lastName: str 
    middleName: Optional[str] 
    email: EmailStr 
    phone: Optional[str] 
    birthday: Optional[date] 


class UserTutorials(Enum):
    system = 'system'
    vcc_page = 'vcc_page'
    meeting_create = 'meeting_create'


class UserUpdateIn(BaseModel):
    login: Optional[Annotated[str, StringConstraints(min_length=4)]] 
    password: Optional[Annotated[str, StringConstraints(min_length=6)]] 
    email: Optional[EmailStr] 
    lastName: Optional[str] 
    firstName: Optional[str] 
    middleName: Optional[str] 
    isActive: Optional[bool]
    roleIds: Optional[List[int]] 
    departmentId: Optional[int] 
    priority: Optional[UserPriority]    
    phone: Optional[str] 
    birthday: Optional[date] 


class ValidationError(BaseModel):
    loc: List[str] 
    msg: str 
    type: str 


class VideoDescription(BaseModel):
    id: str 
    name: str 
    extension: str 
    createdAt: datetime 
    size: Optional[int] 


class VideoDescriptionList(BaseModel):
    data: List[VideoDescription] 


class VinteoFPS(Enum):
    integer_15 = 15
    integer_25 = 25
    integer_30 = 30
    integer_45 = 45
    integer_60 = 60


class VinteoParticipantsLimitOut(BaseModel):
    current: int 
    max: int


class VinteoResolutions(Enum):
    CIF = 'CIF'
    field_4CIF = '4CIF'
    field_640x360 = '640x360'
    field_720p = '720p'
    FULLHD = 'FULLHD'


class VinteoRoomBare(BaseModel):
    id: int 
    callId: str 
    connectUrl: Optional[str]    
    connectCode: int    
    sipDomainUrl: Optional[str]    
    sipIpUrl: Optional[str]    
    organizerNumber: int    
    organizerPassword: str 


class VinteoRoomPublicBare(BaseModel):
    id: int 
    callId: str 
    connectUrl: Optional[str]    
    connectCode: int    
    sipDomainUrl: Optional[str]    
    sipIpUrl: Optional[str]

class VinteoVCSSettingBare(BaseModel):
    id: int 
    needVideoRecording: Optional[bool]


class VinteoVCSSettingCreate(BaseModel):
    needVideoRecording: Optional[bool]


class BuildingFull(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 
    address: Annotated[str, StringConstraints(min_length=1)]   
    municipalAreaId: int 
    municipalArea: CatalogElementBare


class CreateUserIn(BaseModel):
    login: Annotated[str, StringConstraints(min_length=4)] 
    password: Annotated[str, StringConstraints(min_length=6)] 
    email: EmailStr 
    lastName: str 
    firstName: str 
    middleName: Optional[str] 
    phone: Optional[str] 
    birthday: Optional[date] 
    roleIds: List[int] 
    priority: UserPriority    
    departmentId: int 
    isSendEmail: Optional[bool]


class EmailTemplateList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[EmailTemplateOut] 
    sortBy: Optional[str] 


class EventShort(BaseModel):
    startedAt: datetime    
    endedAt: datetime    
    roomId: Optional[int] 
    id: int 
    name: str 
    isOfflineEvent: bool 
    createdUser: UserBrief
    canKickoff: Optional[bool]


class ExternalVCSSettingOut(BaseModel):
    externalUrl: str 
    permanentRoomId: Optional[int] 
    id: int 
    permanentRoom: Optional[PermanentRoomOut] = None


class FileFull(BaseModel):
    name: Annotated[str, StringConstraints(max_length=256)] 
    id: UUID4 
    createdUser: UserBrief


class GroupCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=256)] 
    description: Optional[Annotated[str, StringConstraints(max_length=2048)]] 
    params: Optional[Dict[str, Any]] 
    isPublic: Optional[bool] 
    members: Optional[List[IdMixin]] 
    meetingId: Optional[int] 


class GroupFull(BaseModel):
    id: int 
    name: Annotated[str, StringConstraints(min_length=3, max_length=256)] 
    description: Optional[Annotated[str, StringConstraints(max_length=2048)]] 
    params: Optional[Dict[str, Any]] 
    isPublic: Optional[bool] 
    copiedFromId: Optional[int] 
    membersCount: Optional[int] 
    createdBy: int 
    members: Optional[List[SimpleUserBare]] 


class GroupUpdate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=256)] 
    description: Optional[Annotated[str, StringConstraints(max_length=2048)]] 
    params: Optional[Dict[str, Any]] 
    isPublic: Optional[bool] 
    members: Optional[List[IdMixin]] 


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] 


class LoginOut(BaseModel):
    token: str 
    user: UserInfoOut
    tutorials_progress: Optional[Dict[str, datetime]]

class MeetingBare(BaseModel):
    permalinkId: Optional[str]
    permalink: Optional[str]
    id: Optional[int] 
    name: str 
    roomId: Optional[int] 
    participantsCount: Annotated[Optional[int], Field(ge=1)]  
    sendNotificationsAt: Union[int, datetime]    
    startedAt: datetime    
    endedAt: datetime    
    duration: Optional[int] 
    isGovernorPresents: bool 
    createdAt: datetime 
    closedAt: Optional[datetime] 
    state: MeetingStates 
    organizedBy: Optional[int] 
    createdBy: int 
    isNotifyAccepted: bool 
    isVirtual: Optional[bool]


class MeetingLicense(BaseModel):
    privateLicensesUsedCountRelative: Optional[float]    
    publicLicensesUsedCountRelative: Optional[float]    
    date: date 
    maxLicense: Optional[MeetingLicenseThreshold] = None
    minLicense: Optional[MeetingLicenseThreshold] = None


class MeetingLicenseList(BaseModel):
    data: List[MeetingLicense] 


class MeetingList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[MeetingBare] 
    sortBy: Optional[str] 


class MeetingRecurrenceBrief(BaseModel):
    frequency: MeetingRecurrenceFrequency    
    startedAt: datetime
    interval: Optional[int]    
    count: Optional[int]
    until: Optional[datetime]
    weekDays: Optional[List[MeetingRecurrenceWeekday]]    
    additionalDates: Optional[List[datetime]]
    excludeDates: Optional[List[datetime]]
    id: int 


class MeetingRecurrenceCreate(BaseModel):
    frequency: MeetingRecurrenceFrequency    
    startedAt: datetime
    interval: Optional[int]    
    count: Optional[int]
    until: Optional[datetime]
    weekDays: Optional[List[MeetingRecurrenceWeekday]]    
    additionalDates: Optional[List[datetime]]
    excludeDates: Optional[List[datetime]]


class MeetingShort(BaseModel):
    id: int 
    name: str 
    roomId: Optional[int] 
    room: Optional[RoomShort] = None
    startedAt: datetime    
    endedAt: datetime

class MeetingShortExtended(BaseModel):
    id: int 
    name: str 
    roomId: Optional[int] 
    room: Optional[RoomShort] = None
    startedAt: datetime    
    endedAt: datetime    
    backend: MeetingBackend
    participantsCount: Optional[int] 
    organizedBy: int 
    participants: List[ParticipantOut] 
    organizedUser: Optional[UserBrief] = None


class MeetingStatList(BaseModel):
    data: List[ReportByDate] 


class MeetingUpdateValidated(BaseModel):
    attachments: Optional[List[UUID4]]
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)] 
    roomId: Optional[int] 
    comment: Optional[Annotated[str, StringConstraints(max_length=1000)]] 
    participantsCount: Annotated[Optional[int], Field(ge=1)]  
    sendNotificationsAt: Union[int, datetime]    
    ciscoSettings: Optional[CiscoVCSSettingCreate] = None
    vinteoSettings: Optional[VinteoVCSSettingCreate] = None
    externalSettings: Optional[ExternalVCSSettingCreate]
    startedAt: datetime    
    endedAt: Optional[datetime]    
    duration: Optional[int]    
    isGovernorPresents: Optional[bool]
    isNotifyAccepted: Optional[bool]
    participants: List[Union[ParticipantMock, ParticipantCreate]]
    groups: Optional[List[IdMixin]]
    recurrence: Optional[MeetingRecurrenceCreate]    
    recurrenceUpdateType: Optional[MeetingRecurrenceUpdateType]    
    isVirtual: Optional[bool]


class ParticipantInvolved(BaseModel):
    id: int 
    meeting: Optional[MeetingShort] = None
    groups: Optional[List[GroupBare]] 


class ParticipantsCollisionOut(BaseModel):
    participants: Optional[List[ParticipantInvolved]]

class PermanentRoomList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[PermanentRoomOut] 
    sortBy: Optional[str] 


class PrivateLicenseList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[PrivateLicenseOut] 
    sortBy: Optional[str] 
    name: Optional[str] 


class RoomBare(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 
    buildingId: int 
    maxParticipants: Annotated[Optional[int], Field(ge=1)]  
    isSkitNotified: Optional[bool]
    responsibleUser: Optional[UserBrief] = None


class RoomFull(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=256)] 
    description: Annotated[str, StringConstraints(max_length=1024)] 
    id: int 
    buildingId: int 
    maxParticipants: Annotated[Optional[int], Field(ge=2)]  
    isSkitNotified: Optional[bool]
    responsibleUser: Optional[UserBrief] = None
    building: BuildingBare


class RoomList(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[RoomBare] 
    sortBy: Optional[str] 


class TopByOrganizedUser(BaseModel):
    count: int 
    user: UserBrief


class UserOut(BaseModel):
    id: int 
    login: str 
    lastName: str 
    firstName: str 
    middleName: Optional[str] 
    departmentId: Optional[int] 
    post: Optional[str] 
    email: EmailStr 
    priority: Optional[UserPriority]    
    roleIds: List[int] 
    isActive: bool 
    phone: Optional[str] 
    birthday: Optional[date] 
    createdAt: datetime 
    deletedAt: Optional[datetime] 


class UserOutFull(BaseModel):
    id: int 
    login: str 
    lastName: str 
    firstName: str 
    middleName: Optional[str] 
    departmentId: Optional[int] 
    post: Optional[str] 
    email: EmailStr 
    priority: Optional[UserPriority]   
    roleIds: List[int] 
    isActive: bool 
    phone: Optional[str] 
    birthday: Optional[date] 
    createdAt: datetime 
    deletedAt: Optional[datetime] 
    roles: List[RoleBare] 
    department: Optional[DepartmentBare] = None


class UserOutFullBriefRole(BaseModel):
    id: int 
    login: str 
    lastName: str 
    firstName: str 
    middleName: Optional[str] 
    departmentId: Optional[int] 
    post: Optional[str] 
    email: EmailStr 
    priority: Optional[UserPriority]    
    roleIds: List[int] 
    isActive: bool 
    phone: Optional[str] 
    birthday: Optional[date] 
    createdAt: datetime 
    deletedAt: Optional[datetime] 
    roles: List[CatalogElementBare] 


class UserTutorialMark(BaseModel):
    tutorial: UserTutorials


class VinteoGlobalSettingUpdate(BaseModel):
    backend: MeetingBackend    
    dropEndedConferenceAfter: int
    enableConferenceBefore: int
    maxParticipants: int
    fps: Optional[VinteoFPS]    
    resolution: Optional[VinteoResolutions]

class EventFull(BaseModel):
    isOfflineEvent: bool 
    roomId: Optional[int] 
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)] 
    startedAt: datetime 
    endedAt: Optional[datetime]    
    duration: Annotated[Optional[int], Field(ge=10)]  
    id: int 
    room: Optional[RoomBare] = None


class MeetingCreateValidated(BaseModel):
    attachments: Optional[List[UUID4]] 
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)] 
    roomId: Optional[int] 
    comment: Optional[Annotated[str, StringConstraints(max_length=1000)]] 
    participantsCount: Annotated[Optional[int], Field(ge=1)]  
    sendNotificationsAt: Union[int, datetime]    
    ciscoSettings: Optional[CiscoVCSSettingCreate] = None
    vinteoSettings: Optional[VinteoVCSSettingCreate] = None
    externalSettings: Optional[ExternalVCSSettingCreate]
    startedAt: datetime    
    endedAt: Optional[datetime]    
    duration: Optional[int]    
    isGovernorPresents: Optional[bool]
    isNotifyAccepted: Optional[bool]
    participants: List[Union[ParticipantMock, ParticipantCreate]] 
    groups: Optional[List[IdMixin]]
    recurrence: Optional[MeetingRecurrenceCreate]    
    recurrenceUpdateType: Optional[MeetingRecurrenceUpdateType]    
    isVirtual: Optional[bool]
    state: Optional[MeetingStates] 
    backend: Optional[MeetingBackend] 
    organizedBy: Optional[Union[ParticipantMock, ParticipantCreate]]


class MeetingFull(BaseModel):
    permalinkId: Optional[str]
    permalink: Optional[str] 
    id: Optional[int] 
    name: str 
    roomId: Optional[int] 
    participantsCount: Annotated[Optional[int], Field(ge=1)]  
    sendNotificationsAt: Union[int, datetime]    
    startedAt: datetime    
    endedAt: datetime    
    duration: Optional[int] 
    isGovernorPresents: bool 
    createdAt: datetime 
    closedAt: Optional[datetime] 
    state: MeetingStates 
    organizedBy: Optional[int] 
    createdBy: int 
    isNotifyAccepted: bool 
    isVirtual: Optional[bool]
    organizerPermalinkId: Optional[str]
    organizerPermalink: Optional[str]
    comment: Optional[str] 
    event: EventBare
    room: Optional[RoomBare] = None
    ciscoRoom: Optional[CiscoRoomBare] = None
    ciscoSettings: Optional[CiscoVCSSettingBare] = None
    vinteoRoom: Optional[VinteoRoomBare] = None
    vinteoSettings: Optional[VinteoVCSSettingBare] = None
    externalSettings: Optional[ExternalVCSSettingOut] = None
    participants: List[ParticipantOut] 
    attachments: List[FileBare] 
    groups: List[GroupBare] 
    ciscoSettingsId: Optional[int] 
    ciscoRoomId: Optional[int] 
    eventId: int 
    updatedAt: datetime 
    backend: Optional[MeetingBackend] 
    createdUser: UserBrief
    organizedUser: Optional[UserBrief] = None
    recurrence: Optional[MeetingRecurrenceBrief]

class MeetingPermalinkOrganizerFull(BaseModel):
    id: int 
    name: str 
    roomId: Optional[int] 
    room: Optional[RoomFull] = None
    participantsCount: Annotated[Optional[int], Field(ge=1)]  
    startedAt: datetime    
    endedAt: datetime    
    duration: Optional[int] 
    state: MeetingStates 
    ciscoRoom: Optional[CiscoRoomBare] = None
    vinteoRoom: Optional[VinteoRoomBare] = None
    externalSettings: Optional[ExternalVCSSettingOut] = None
    participants: List[ParticipantOut] 
    ciscoSettingsId: Optional[int] 
    vinteoSettingsId: Optional[int] 
    ciscoRoomId: Optional[int] 
    vinteoRoomId: Optional[int] 
    eventId: int 
    backend: Optional[MeetingBackend] 
    organizer: UserBrief
    link: Optional[str]
    organizerLink: Optional[str]
    enableConferenceBefore: Optional[int]


class MeetingPermalinkOut(BaseModel):
    id: int 
    name: str 
    roomId: Optional[int] 
    room: Optional[RoomFull] = None
    startedAt: datetime    
    endedAt: datetime    
    ciscoRoom: Optional[CiscoRoomPublicBare] = None
    vinteoRoom: Optional[VinteoRoomPublicBare] = None
    externalSettings: Optional[ExternalVCSSettingOut] = None
    participantsCount: Annotated[Optional[int], Field(ge=1)]  
    duration: Optional[int] 
    backend: Optional[MeetingBackend] 
    state: MeetingStates 
    organizer: UserBrief
    link: Optional[str]
    enableConferenceBefore: Optional[int]


class UserListOut(BaseModel):
    rowsPerPage: Optional[int] 
    page: Optional[int] 
    rowsNumber: Optional[int] 
    showDeleted: Optional[bool] 
    data: List[UserOutFullBriefRole] 
    sortBy: Optional[str] 