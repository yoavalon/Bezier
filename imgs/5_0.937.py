d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)

d.end()
