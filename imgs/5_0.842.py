d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.S, Length.short)
d.position_pen(0,2)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
