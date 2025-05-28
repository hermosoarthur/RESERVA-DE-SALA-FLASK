from flask import Blueprint, request, jsonify
from reserva_model import Reserva
from database import db
import requests
import os

routes = Blueprint("routes", __name__)

API_TURMAS_URL = ("http://api-flask:5000")


def validar_turma(turma_id):
    try:
        resp = requests.get(
            f"{API_TURMAS_URL}/projeto-api-flask/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Erro ao validar turma: {e}")
        return False


@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201


@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])


@routes.route("/reservas/<int:id>", methods=["GET"])
def obter_reserva(id):
    reserva = Reserva.query.get(id)
    if reserva:
        return jsonify({
            "id": reserva.id,
            "turma_id": reserva.turma_id,
            "sala": reserva.sala,
            "data": reserva.data,
            "hora_inicio": reserva.hora_inicio,
            "hora_fim": reserva.hora_fim
        })
    else:
        return jsonify({"erro": "Reserva não encontrada"}), 404


@routes.route("/reservas", methods=["DELETE"])
def deletar_todas_reservas():
    try:
        num_apagadas = Reserva.query.delete()
        db.session.commit()
        return jsonify({"mensagem": "reservas apagadas com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
