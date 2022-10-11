d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(2,0)
d.straight_line(Direction.SE, Length.short)

d.end()
