from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import UpdateProcessView,CreateProcessView

from . import views
from .models import DocumentUploadProcess


@frontend.register
class DocumentUploadFlow(Flow):
    process_class = DocumentUploadProcess

    start = (
        flow.Start(
            views.start_upload_workflow
            #CreateProcessView,
            #fields=["text"]
        ).Permission(
            #auto_create=True
            'munshai.add_helloworldprocess'
            #'munshai.can_start_helloworldprocess',
            #'munshai.can_view_helloworldprocess'
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved", "upload"]
        ).Permission(
            #auto_create=True
            'munshai.can_approve_helloworldprocess',
            #'munshai.can_approve_helloworldprocess'
            #'munshai.view_helloworldrocess'
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
            .Then(this.send)
            .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_hello_world_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_hello_world_request(self, activation):
        print(activation.process.text)
        print(activation.process.upload)
        # activation.process.
