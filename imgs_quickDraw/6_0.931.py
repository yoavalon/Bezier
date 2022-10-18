d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.short)
d.position_pen(3,3)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
