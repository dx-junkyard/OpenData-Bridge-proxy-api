
try:
    from repository import UniversalMenuRepository
    from domain import UniversalMenuDomain
except:
    from .repository import UniversalMenuRepository
    from .domain import UniversalMenuDomain

class UniversalMenuService(object):
    def __init__(self):
        self.repository = UniversalMenuRepository()
        
    def get(self, city) -> UniversalMenuDomain:
        corporateCode = self.repository.getCorporateCode(city)
        groupCode = self.repository.getGroupCode(city)

        return UniversalMenuDomain(
            corporateCode=corporateCode,
            groupCode=groupCode
        )
