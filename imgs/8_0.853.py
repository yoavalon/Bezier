d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
