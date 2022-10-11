d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,1)

d.end()
