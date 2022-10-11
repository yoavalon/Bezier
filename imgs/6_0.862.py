d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
