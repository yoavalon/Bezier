d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,0)

d.end()
