aggregate, valueObj, entity, workflow, dto = BounderContextTools()
createDto, details, summary, update = dtos.get_standard

@aggregate:
class User:

    # all value obj is in details dto
    @valueObj.default("") # if a value obj has one defualt val => this props isnt in create dto
    @valueObj.basicProps  # if value obj is a basic props => this props is in summaty dto
    @valueObj.readonly    # if value obj is readonly props => this props isnt in update dto
    @entity.required_col  # No nuleable column
    @entity.unique_col    # unique column
    name = str()

@workflow(
    input= (createDto,),
    output= None
)
def use_create_use_case(dto, domain, mapper, repo):
    user_domain = domain.create(dto)
    user_entity = mapper.to_persistent(user_domain)
    repo.save(user_entity)

    
