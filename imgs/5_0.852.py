d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.short)
d.position_pen(1,0)
d.straight_line(Direction.NW, Length.medium)

d.end()
