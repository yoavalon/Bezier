d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
