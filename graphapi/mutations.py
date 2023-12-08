import graphene
from graphql import GraphQLError

from restapi.models import  Me, Project, Pricing, Skill, Contact
from .modeltypes import(
    MeType,
    ProjectType,
    PricingType,
    SkillType,
    ContactType,
)
   
class CreateMe(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        instagram = graphene.String()
        github = graphene.String()
        linkedin = graphene.String()
        telegram = graphene.String()
        education = graphene.String()
        work_history = graphene.String()
    
    me = graphene.Field(MeType)
    
    def mutate(self, info, first_name, last_name, email, phone, **kwargs):
        me = Me(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            instagram=kwargs.get('instagram'),
            github=kwargs.get('github'),
            linkedin=kwargs.get('linkedin'),
            telegram=kwargs.get('telegram'),
            education=kwargs.get('education'),
            work_history=kwargs.get('work_history'),
        )
        me.save()
        return CreateMe(me=me)
    
class UpdateMe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        instagram = graphene.String()
        github = graphene.String()
        linkedin = graphene.String()
        telegram = graphene.String()
        education = graphene.String()
        work_history = graphene.String()
    
    me = graphene.Field(MeType)
    
    def mutate(self, info, id, **kwargs):
        try:
            me = Me.objects.get(id=id)
        except Me.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        me.first_name = kwargs.get('first_name', me.first_name)
        me.last_name = kwargs.get('last_name', me.last_name)
        me.email = kwargs.get('email', me.email)
        me.phone = kwargs.get('phone', me.phone)
        me.instagram = kwargs.get('instagram', me.instagram)
        me.github = kwargs.get('github', me.github)
        me.linkedin = kwargs.get('linkedin', me.linkedin)
        me.telegram = kwargs.get('telegram', me.telegram)
        me.education = kwargs.get('education', me.education)
        me.work_history = kwargs.get('work_history', me.work_history)
        
        me.save()
        return UpdateMe(me=me)
    
class DeleteMe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    success = graphene.Boolean()
        
    def mutate(self, info, id):
        try:
            me = Me.objects.get(id=id)
        except Me.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        me.delete()
        return DeleteMe(success = True)
       
####################    
    
class CreateProject(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        start_date = graphene.Date(required=True)
        file = graphene.String()
        image = graphene.String()
        end_date = graphene.Date()
        url = graphene.String()
        repository = graphene.String()
        technologies_used = graphene.String()
    
    project = graphene.Field(ProjectType)
    
    def mutate(self, info, title, description, start_date, **kwargs):
        project = Project(
            title=title,
            description=description,
            start_date=start_date,
            file=kwargs.get('file'),
            image=kwargs.get('image'),
            end_date=kwargs.get('end_date'),
            url=kwargs.get('url'),
            repository=kwargs.get('repository'),
            technologies_used=kwargs.get('technologies_used'),
        )
        project.save()
        return CreateProject(project=project) 

class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        start_date = graphene.Date()
        file = graphene.String()
        image = graphene.String()
        end_date = graphene.Date()
        url = graphene.String()
        repository = graphene.String()
        technologies_used = graphene.String()
    
    project = graphene.Field(ProjectType)
    
    def mutate(self, info, id, **kwargs):
        try:
            project = Project.objects.get(id=id)
        except Project.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        project.title = kwargs.get('title', project.title)
        project.description = kwargs.get('description', project.description)
        project.start_date = kwargs.get('start_date', project.start_date)
        project.file = kwargs.get('file', project.file)
        project.image = kwargs.get('image', project.image)
        project.end_date = kwargs.get('end_date', project.end_date)
        project.url = kwargs.get('url', project.url)
        project.repository = kwargs.get('repository', project.repository)
        
class DeleteProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
        
    def mutate(self, info, id):
        try:
            project = Project.objects.get(id=id)
        except Project.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        project.delete()
        return DeleteProject(success = True)
    
#####################################

class CreatePricing(graphene.Mutation):
    class Arguments:
        service = graphene.String(required=True)
        description = graphene.String(required=True)
        rate_per_hour = graphene.Decimal(required=True)
        estimated_hours  = graphene.Decimal(required=True)
    
    pricing = graphene.Field(PricingType)
    
    def mutate(self, info, service, description, rate_per_hour, estimates_hours):
        pricing = Pricing(
            service=service,
            description=description,
            rate_per_hour=rate_per_hour,
            estimated_hours=estimates_hours,
        )
        pricing.save()
        return CreatePricing(pricing=pricing)
    
    
class UpdatePricing(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        service = graphene.String()
        description = graphene.String()
        rate_per_hour = graphene.Decimal()
        estimated_hours  = graphene.Decimal()
    
    pricing = graphene.Field(PricingType)
    
    def mutate(self, info, id, **kwargs):
        try:
            pricing = Pricing.objects.get(id=id)
        except Pricing.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        pricing.service = kwargs.get('service', pricing.service)
        pricing.description = kwargs.get('description', pricing.description)
        pricing.rate_per_hour = kwargs.get('rate_per_hour', pricing.rate_per_hour)
        pricing.estimated_hours = kwargs.get('estimated_hours', pricing.estimated_hours)
        
        pricing.save()
        
        return UpdatePricing(pricing=pricing)
    
    
class DeletePricing(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    success = graphene.Boolean()
        
    def mutate(self, info, id):
        try:
            pricing = Pricing.objects.get(id=id)
        except Pricing.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        pricing.delete()
        return DeletePricing(success = True)
    
#######################

class CreateSkill(graphene.Mutation):
    class Arguments:
        category = graphene.String(required=True)
        name = graphene.String(required=True)
        percentage = graphene.Int(required=True)
        
    skill = graphene.Field(SkillType)
    
    def mutate(self, info, category, name, percentage):
        skill = Skill(
            category=category,
            name=name,
            percentage=percentage,
        )
        skill.save()
        return CreateSkill(skill=skill)
    
class UpdateSkill(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        category = graphene.String()
        name = graphene.String()
        percentage = graphene.Int()
    
    skill = graphene.Field(SkillType)
    
    def mutate(self, info, id, **kwargs):
        try:
            skill = Skill.objects.get(id=id)
        except Skill.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        skill.category = kwargs.get('category', skill.category)
        skill.name = kwargs.get('name', skill.name)
        skill.percentage = kwargs.get('percentage', skill.percentage)
        
        skill.save()
        
        return UpdateSkill(skill=skill)
    
class DeleteSkill(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    success = graphene.Boolean()
        
    def mutate(self, info, id):
        try:
            skill = Skill.objects.get(id=id)
        except Skill.DoesNotExist:
            raise GraphQLError(f"Информация с id {id} не существует")
        
        skill.delete()
        return DeleteSkill(success = True)
    
##########################


class CreateContact(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        subject = graphene.String(required=True)
        message = graphene.String(required=True)

    contact = graphene.Field(ContactType)

    def mutate(self, info, name, email, subject, message):
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        contact.save()

        return CreateContact(contact=contact)
    
    
class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        subject = graphene.String()
        message = graphene.String()

    contact = graphene.Field(ContactType)

    def mutate(self, info, id, **kwargs):
        try:
            contact = Contact.objects.get(pk=id)
        except Contact.DoesNotExist:
            raise GraphQLError(f"Контакт с идентификатором {id} не существует.")

        contact.name = kwargs.get('name', contact.name)
        contact.email = kwargs.get('email', contact.email)
        contact.subject = kwargs.get('subject', contact.subject)
        contact.message = kwargs.get('message', contact.message)

        contact.save()

        return UpdateContact(contact=contact)
    

class DeleteContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            contact = Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            raise GraphQLError(f"Контакт с идентификатором {id} не существует.")

        contact.delete()

        return DeleteContact(success=True)

    
class Mutation(graphene.ObjectType):
    create_me = CreateMe.Field()
    update_me = UpdateMe.Field()
    delete_me = DeleteMe.Field()
    
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
    
    create_pricing = CreatePricing.Field()
    update_pricing = UpdatePricing.Field()
    delete_pricing = DeletePricing.Field()
    
    create_skill = CreateSkill.Field()
    update_skill = UpdateSkill.Field()
    delete_skill = DeleteSkill.Field()
    
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    delete_contact = DeleteContact.Field()
    
        
        
    


    


        
        


    

        
                               

    


