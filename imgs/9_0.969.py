d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)

d.end()
