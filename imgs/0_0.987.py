d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)

d.end()
