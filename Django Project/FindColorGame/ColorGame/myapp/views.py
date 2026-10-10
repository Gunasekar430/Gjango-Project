import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models import GameResult


def home(request):
    return render(request, 'index.html')


@require_POST
def save_result(request):
    try:
        data = json.loads(request.body)

        player_name = data.get('player_name', '').strip()
        score = int(data.get('score', 0))
        treasures_found = int(data.get('treasures_found', 0))
        moves = int(data.get('moves', 0))

        if not player_name:
            return JsonResponse({
                'success': False,
                'message': 'Player name is required'
            }, status=400)

        result = GameResult.objects.create(
            player_name=player_name,
            score=max(score, 0),
            treasures_found=max(treasures_found, 0),
            moves=max(moves, 0)
        )

        return JsonResponse({
            'success': True,
            'id': result.id
        })

    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({
            'success': False,
            'message': 'Invalid data'
        }, status=400)


@require_GET
def leaderboard(request):
    results = GameResult.objects.order_by(
        '-score',
        '-treasures_found',
        'played_at'
    )[:5]

    data = []

    for index, result in enumerate(results, start=1):
        data.append({
            'rank': index,
            'player_name': result.player_name,
            'score': result.score,
            'treasures_found': result.treasures_found,
            'moves': result.moves,
        })

    return JsonResponse(data, safe=False)